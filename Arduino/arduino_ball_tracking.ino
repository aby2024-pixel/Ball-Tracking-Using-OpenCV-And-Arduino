#include <Servo.h>

Servo cameraServo;

void setup() {
  Serial.begin(9600);
  cameraServo.attach(9);  // Attach to digital pin 9
  cameraServo.write(90);  // Start at the center position
}

void loop() {
  if (Serial.available() > 0) {
    char direction = Serial.read();
    if (direction == 'L') {
      cameraServo.write(45);  // Rotate left
    } else if (direction == 'R') {
      cameraServo.write(135);  // Rotate right
    } else if (direction == 'S') {
      cameraServo.write(90);   // Center position (stop)
    }
  }
}
