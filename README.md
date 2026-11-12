EMG-Controlled Unity Interaction

A real-time electromyography (EMG) control system that translates muscle activity into binary control signals for object interaction in Unity. The system integrates OpenBCI Ganglion, Python, Lab Streaming Layer (LSL), and UDP communication.

Project Structure

EMG-Controlled-Unity/
├── Python/
│   └── main.py
├── Unity/
│   └── WebSocketReceiver.cs
└── README.md

System Architecture

OpenBCI Ganglion
       ↓
      LSL
       ↓
Python (main.py)
       │
       ├── Filtering
       ├── Rectification
       ├── RMS Calculation
       └── Threshold Detection
       ↓
Binary Output (0/1)
       ↓
      UDP
       ↓
Unity (WebSocketReceiver.cs)
       ↓
Object Interaction

Implementation

Python — main.py

Acquires EMG data through LSL and processes the signal using filtering, rectification, and root mean square (RMS) calculations. A predefined threshold converts muscle activity into binary activation states (0/1), which are transmitted to Unity via UDP.

Unity — WebSocketReceiver.cs

Receives the processed activation states and maps them to object interactions within the Unity environment, separating signal processing from application-level control.

Technology Stack

* Hardware: OpenBCI Ganglion, EMG electrodes
* Languages: Python, C#
* Frameworks/Tools: Unity, Lab Streaming Layer (LSL)
* Communication: UDP

Current Capabilities

* Real-time EMG acquisition and processing
* RMS-based muscle activation detection
* Binary control signal generation
* UDP communication between Python and Unity
* Real-time Unity object interaction

Future Development

* Adaptive thresholding and hysteresis
* Multichannel and multi-level EMG classification
* Real-time signal visualization and latency analysis
* State-machine-based control
* ESP32-based embedded implementation