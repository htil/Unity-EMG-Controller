EMG-Controlled Unity Interaction

Real-time EMG control system using an OpenBCI Ganglion, Python, LSL, UDP, and Unity.

Code Layout

EMG-Controlled-Unity/
│
├── Python/
│   └── main.py
│
├── Unity/
│   └── WebSocketReceiver.cs
│
└── README.md

Data Flow

OpenBCI Ganglion
       │
       ▼
      LSL
       │
       ▼
    main.py
       │
       ├── Filter
       ├── Rectify
       ├── RMS
       └── Threshold
       │
       ▼
     0 / 1
       │
       ▼
      UDP
       │
       ▼
WebSocketReceiver.cs
       │
       ▼
   Unity Object

Python

main.py

Processes the incoming EMG stream and converts muscle activity into a digital activation signal.

Pipeline:

EMG Signal
    ↓
Filtering
    ↓
Rectification
    ↓
RMS
    ↓
Threshold
    ↓
Binary Output

The resulting 0/1 activation state is transmitted to Unity over the network.

Unity

WebSocketReceiver.cs

Receives the control signal from the Python processing pipeline and maps the activation state to an object interaction inside Unity.

The receiver acts as the interface between the external EMG system and the Unity application.

Note: If this script communicates directly using UDP, rename it to UDPReceiver.cs so the filename matches the implementation.

Hardware

* OpenBCI Ganglion
* EMG electrodes
* Computer running the Python processing pipeline
* Computer running Unity

Software

* Python
* Unity
* C#
* Lab Streaming Layer (LSL)
* UDP

System Overview

The project separates signal acquisition, signal processing, network communication, and visualization/control into distinct stages.

This allows the EMG signal to be processed independently from the Unity application while maintaining real-time interaction.

Current Functionality

* Real-time EMG acquisition
* LSL data streaming
* EMG filtering
* Signal rectification
* RMS calculation
* Threshold-based activation detection
* Network transmission
* Unity object control

Future Improvements

* Adaptive thresholds
* Hysteresis for more stable activation
* Multi-level EMG control
* Multiple EMG channels
* Real-time signal visualization
* End-to-end latency measurements
* State-machine based control
* Embedded implementation using ESP32