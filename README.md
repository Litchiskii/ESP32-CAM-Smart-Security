# ESP32 CAM Based Face & Eyes Recognition System

This project implements a **face, eye, and intruder recognition system** using the ESP32-CAM module and Python for live video processing. The system also recognizes known individuals and flags intruders.

## Overview

The system streams live video from the ESP32-CAM module. Python scripts process these frames to detect faces and eyes and classify recognized faces against a known dataset to determine whether the person is recognized or an intruder.

### Key Components:
- ESP32-CAM Module
- Python for frame processing and recognition (using OpenCV)
- Intruder recognition system based on a dataset of known individuals

## Features
- Face and eye detection
- Intruder recognition based on a local dataset
- Live video streaming
- High-resolution transmission option

## Components
1. **ESP32-CAM Board**
2. **FTDI Programmer**
3. **Jumper Wires**
4. **Micro-USB Cable**

## Wiring Setup
Connect the ESP32-CAM and FTDI module as follows:

| ESP32-CAM Pin | FTDI Pin  |
|---------------|-----------|
| GND           | GND       |
| 5V            | VCC (5V)  |
| U0R           | TX        |
| U0T           | RX        |
| GPIO 0        | GND       |

## Installation & Setup

### Arduino IDE:
1. Install the ESP32-CAM library from [GitHub](https://github.com/espressif/arduino-esp32).
2. Upload the code (`esp32cam_face_recognition.ino`) to the ESP32-CAM.

### Python:
1. Install Python 3.7 or above.
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt

# WifiCam: WiFi camera HTTP server

This example runs on ESP32-CAM board.
It provides an HTTP server where you can access BMP, JPG, and MJPEG formats in various resolutions.
To use this example, modify WiFi SSID+password, then upload to ESP32.

ESP32 `WebServer` can only serve one TCP connection at a time.
If you have accessed an MJPEG stream in a browser, you need to click *Stop* button to terminate the connection.
Otherwise, you won't be able to open another page or picture.

Due to memory constraints, it's not recommended to access BMP format in high resolution.
