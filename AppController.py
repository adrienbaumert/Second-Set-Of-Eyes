# Performing necessary imports
from PictureTaking import PictureTaker
from TextToSpeech import Speaker
from ImageCaptioning import ImageCaptioner

class Controller:
    def __init__(self):
        self.snapshot = PictureTaker()
        self.speaker = Speaker()
        self.captioner = ImageCaptioner()

    # Taking a picture and turning it into speech
    def takingPictureToSpeech(self):
        self.snapshot.takePicture()
        text = self.captioner.query("Images/test.jpg")

        text = text[0]["generated_text"]
        self.speaker.tts(text)