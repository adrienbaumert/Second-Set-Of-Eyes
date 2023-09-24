# Performing necessary imports
from PictureTaking import PictureTaker
from TextToSpeech import Speaker
from ImageCaptioning import ImageCaptioner

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

    def runApp(self):
        self.app.run()

    # Taking a picture and turning it into speech
    def takingPictureToSpeech(self):
        # Handles any errors
        try:
            self.snapshot.takePicture()
            text = self.captioner.query("Images/picture.jpg")

            path = self.speaker.tts(text)

            self.finished = True

            self.speaker.speak(path)

        except:
            path = self.speaker.tts("Image Captioning API is currently busy. Please try again.")

            self.finished = True

            self.speaker.speak(path)

    def checkFinished(self):
        return self.finished

    def setFinishedFalse(self):
        self.finished = False