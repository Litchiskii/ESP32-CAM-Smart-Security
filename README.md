# ESP32 CAM Based Face & Eyes Recognition System

This project implements a **face and eye recognition system** using the ESP32-CAM module and Python for live video processing.

## Overview

This system utilizes the ESP32-CAM module to stream live video, and a Python script to process the frames to detect faces and eyes. The system highlights faces in red and eyes in green.

### Key Components:
- ESP32-CAM Module
- Python for frame processing (using OpenCV)

## Features
- Face detection
- Eye detection
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
