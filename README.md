# Ball-Tracking-Using-OpenCV-And-Arduino
# Ball Tracking System using OpenCV and Arduino

This project implements a real-time ball tracking system using Python with OpenCV for image processing and Arduino for controlling camera movements.

## Requirements
- Python 3.x
- Arduino Uno
- Web Camera
- Libraries: OpenCV, numpy, pyserial

## Setup
1. Install the required Python dependencies by running:
   pip install -r requirements.txt

2. Upload the Arduino code (`arduino_ball_tracking.ino`) to your Arduino board.
3. Run the Python script:
   python ball_tracking.py
   
## How it Works
The system detects a colored ball using OpenCV, processes its position, and sends commands to the Arduino to adjust the camera accordingly.

## License
This project is licensed under the MIT License.
