import socket
import numpy as np
from scipy.signal import butter, lfilter
from collections import deque
from pylsl import StreamInlet, resolve_streams


# Electrode setup notes:
# - Black (reference): back of hand between middle and pinky fingers
# - Red (channel 1): 4 inches below brown on forearm
# - Brown (channel 2): middle of forearm, palm facing up
# This setup picks up hand/forearm muscle activation

# Send activation state to Unity

UDP_IP = "127.0.0.1"   # localhost - same machine running Unity
UDP_PORT = 5005        # listening port in Unity
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ganglion specs and signal processing settings

FS = 200              # Ganglion samples at 200 Hz
BUFFER_SIZE = 20      # ~100ms window for processing
THRESHOLD = 10        # TODO:  calibrate this after testing live data

# Bandpass to isolate muscle signal (filtering out noise and DC drift)

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return b, a

def bandpass_filter(data, lowcut=20, highcut=95):
    b, a = butter_bandpass(lowcut, highcut, FS)
    return lfilter(b, a, data)

# ==============================
# RMS Feature Extraction
# ==============================
def rms(signal):
    # RMS captures signal amplitude - good indicator of muscle activation
    return np.sqrt(np.mean(np.square(signal)))

# Grab the LSL stream from OpenBCI GUI

print("Searching for OpenBCI Ganglion LSL stream...")
streams = resolve_streams()
if not streams:
    print("No LSL streams found!")
    exit()
inlet = StreamInlet(streams[0])
print("Connected to Ganglion via LSL!")

# Using channel 2 (index 1) - that's where I have the muscle sensor
EMG_CHANNEL = 1

buffer = deque(maxlen=BUFFER_SIZE)

print("\nProcessing EMG and sending to Unity...\n")

# Main processing loop

while True:
    sample, timestamp = inlet.pull_sample()
    emg = sample[EMG_CHANNEL]

    buffer.append(emg)

    # Process once buffer is full
    if len(buffer) == BUFFER_SIZE:
        data = np.array(buffer)
        
        # Signal processing pipeline:
        # 1. Filter out noise
        filtered = bandpass_filter(data)
        # 2. Make everything positive (we only care about amplitude)
        rectified = np.abs(filtered)
        # 3. Calculate overall signal strength
        feature = rms(rectified)
        
        # Threshold for muscle activation - tune this based on resting vs flexed readings
        THRESHOLD = .10
        # 4. Binary decision: is the muscle activating?
        state = 1 if feature >= THRESHOLD else 0
        
        # Show what's happening
        print(f"Feature: {feature:.2f} | State: {state}")
        
        # Send state to Unity

        sock.sendto(str(state).encode(), (UDP_IP, UDP_PORT))
