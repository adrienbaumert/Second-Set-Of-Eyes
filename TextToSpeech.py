# Importing necessary libraries
from gtts import gTTS
from playsound import playsound

# Class that goes from text to speech and can play speech
class Speaker:
    def tts(self, text):
        speech = gTTS(text=text, lang="en")
        speech.save("Speech/speech.mp4")

        return "Speech/speech.mp4"

    def speak(self, text):
        playsound(text)
