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

    # Taking a picture and turning it into speech
    def takingPictureToSpeech(self):
        # Handles any errors
        try:
            self.snapshot.takePicture()
            text = self.captioner.query("Images/picture.jpg")

            path = self.speaker.tts(text)
            self.speaker.speak(path)

        except:
            path = self.speaker.tts("There was an error, please try again.")
            self.speaker.speak(path)
