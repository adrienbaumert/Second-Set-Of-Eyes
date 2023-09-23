# Importing necessary libraries
import cv2

class PictureTaker:
    def takePicture(self):
        # Setting camera to default camera
        self.cap = cv2.VideoCapture(0)

        # Setting the camera frame rate
        self.cap.set(cv2.CAP_PROP_FPS, 30)

        # Setting the camera buffer limit
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        # Taking a picture
        ret, frame = self.cap.read()

        # Saving the picture to a location
        cv2.imwrite("Images/picture.jpg", frame)

        # Releasing the camera
        self.cap.release()