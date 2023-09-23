# Importing necessary libraries
from gtts import gTTS

class Speaker:
    def tts(self, text):
        speech = gTTS(text=text, lang="en")

        speech.save("Speech/speech.mp4")