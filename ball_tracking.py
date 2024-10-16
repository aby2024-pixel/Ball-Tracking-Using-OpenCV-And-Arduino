import cv2
import numpy as np
import serial
import time

# Set up serial communication with Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your Arduino port
arduino.flush()

time.sleep(2)  # Allow time for the serial connection to initialize

# Set up the video capture
cap = cv2.VideoCapture(0)  # Use the default webcam

# Define the lower and upper boundaries for the color of the ball in HSV color space
# Adjust these values based on the color of the ball
lower_color = np.array([29, 86, 6])
upper_color = np.array([64, 255, 255])

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame and convert it to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the color of the ball
        mask = cv2.inRange(hsv, lower_color, upper_color)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
           
        if len(contours) > 0:
            # Find the largest contour in the mask
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Only proceed if the radius meets a minimum size
            if radius > 10:
                # Draw the circle and centroid on the frame
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

                # Determine the direction based on the position of the ball
                if x < frame.shape[1] / 3:
                    direction = 'L'  # Move left
                elif x > 2 * frame.shape[1] / 3:
                    direction = 'R'  # Move right
                else:
                    direction = 'S'  # Stop

                # Send the direction to the Arduino
                arduino.write(direction.encode())

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stopped by User")

finally:
    # When everything is done, release the capture and close serial communication
    cap.release()
    arduino.close()
    cv2.destroyAllWindows()

