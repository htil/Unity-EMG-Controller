# Unity-EMG-Controller
# EMG-Controlled Unity Interaction

This project uses EMG signals from an OpenBCI Ganglion to control a Unity object in real time.

## How It Works

EMG data is streamed via LSL, processed in Python, and converted into a binary activation signal:

- Filter → Rectify → RMS → Threshold → 0/1 output

The result is sent to Unity to trigger movement.

## Files

- `main.py` — processes EMG and sends data (UDP)  
- `WebSocketReceiver.cs` — receives data in Unity and moves object  

## Setup

Python:
