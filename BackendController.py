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
# File: BackendController.py
# Version : 1.0.0
# =================================================
# Performing necessary imports
from PictureTaking import PictureTaker
from TextToSpeech import Speaker
from ImageCaptioning import ImageCaptioner
import time

# Class that controls the app
class Controller:
    def __init__(self):
        self.snapshot = PictureTaker()
        self.speaker = Speaker()
        self.captioner = ImageCaptioner()

        # Making a flag that turns true when one loop of controller
        # is made
        # Finished flag is made so that processing function in VisionImparedApp.py
        # can know when to stop
        self.finished = False

    # Taking a picture and turning it into speech
    def takingPictureToSpeech(self):
        # Handles any errors
        try:
            self.snapshot.takePicture()
            text = self.captioner.query("Images/picture.jpg")

            path = self.speaker.tts(text)

            self.finished = True

            # Sleeping for one second so that audible processing can
            # finish playing
            time.sleep(1)

            self.speaker.speak(path)

        except:
            path = self.speaker.tts("Image Captioning API is currently busy. Please try again.")

            self.finished = True

            # Sleeping for one second so that audible processing can
            # finish playing
            time.sleep(1)

            self.speaker.speak(path)

    def checkFinished(self):
        return self.finished

    def setFinishedFalse(self):
        self.finished = False