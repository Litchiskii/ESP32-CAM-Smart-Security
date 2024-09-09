# ESP32 CAM Based Face & Eyes Recognition System

This project implements a **face, eye, and intruder recognition system** using the ESP32-CAM module and Python for live video processing. The system recognizes known individuals from a pre-built dataset and flags unrecognized individuals as intruders.

## Features
- Face and eye detection with OpenCV
- Intruder recognition using a known face dataset
- Live video streaming with adjustable resolution

## Components
- **ESP32-CAM Board**
- **FTDI Programmer**
- **Jumper Wires**
- **Micro-USB Cable**

## Setup Instructions

### 1. Wiring
Connect the ESP32-CAM and FTDI programmer as follows:

| ESP32-CAM Pin | FTDI Pin  |
|---------------|-----------|
| GND           | GND       |
| 5V            | VCC (5V)  |
| U0R           | TX        |
| U0T           | RX        |
| GPIO 0        | GND       |

### 2. Arduino IDE
1. Install the ESP32-CAM library from [GitHub](https://github.com/espressif/arduino-esp32).
2. Upload the provided Arduino code (`esp32cam_face_recognition.ino`) to the ESP32-CAM.

### 3. Python Setup
1. Install Python 3.7 or above.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
 IP Address Configuration
After uploading the Arduino code, retrieve the IP address from the Serial Monitor in the Arduino IDE.
Update the Python scripts with the correct IP address:
Open face_eye_recognition.py and intruder_recognition.py.
Replace <YOUR_IP> in the url variable with the IP from the Serial Monitor:
python
Copy code
url = 'http://<YOUR_IP>/cam-lo.jpg'
5. Dataset Setup for Known Faces
Create a directory Dataset/ in the project root.
Inside Dataset/, create a subfolder called known_faces/.
For each known person, create a separate folder with their name and place their images inside
