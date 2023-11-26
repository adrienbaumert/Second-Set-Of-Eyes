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
import os
from dotenv import load_dotenv
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

        # Loading .env file
        load_dotenv()

        # Setting a image/speech directory constant to the value of the key
        # stored in the .env file
        self.IMAGE_DIRECTORY = os.getenv("IMAGE_DIRECTORY", "image_directory")
        self.SPEECH_DIRECTORY = os.getenv("SPEECH_DIRECTORY", "speech_directory")

    # Taking a picture and turning it into speech
    def takingPictureToSpeech(self):
        # Handles any errors
        try:
            self.snapshot.takePicture(self.IMAGE_DIRECTORY)
            text = self.captioner.query(self.IMAGE_DIRECTORY)

            # Saving the spoken text to the speech directory
            self.speaker.tts(text, self.SPEECH_DIRECTORY)

            self.finished = True

            # Sleeping for one second so that audible processing can
            # finish playing
            time.sleep(1)

            self.speaker.speak(self.SPEECH_DIRECTORY)

        except:
            path = self.speaker.tts("Image Captioning API is currently busy. Please try again.", self.SPEECH_DIRECTORY)

            self.finished = True

            # Sleeping for one second so that audible processing can
            # finish playing
            time.sleep(1)

            self.speaker.speak(self.SPEECH_DIRECTORY)

    def checkFinished(self):
        return self.finished

    def setFinishedFalse(self):
        self.finished = False