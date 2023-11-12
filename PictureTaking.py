# Copyright (C) 2023 Adrien Baumert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Project: Second-Set-Of-Eyes
# File: PictureTaking.py
# Version : 1.0.0
# =================================================
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

        # [TESTING]
        import os
        # Create 'Images' directory if it does not exist
        if not os.path.exists('Images'):
            os.makedirs('Images')

        # Saving the picture to a location
        cv2.imwrite("Images/picture.jpg", frame)

        # Releasing the camera
        self.cap.release()