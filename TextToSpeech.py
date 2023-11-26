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
# File: TextToSpeech.py
# Version : 1.1.0
# =================================================
# Importing necessary libraries
from gtts import gTTS
from playsound import playsound

# Class that goes from text to speech and can play speech
class Speaker:
    def tts(self, text, directory):
        speech = gTTS(text=text, lang="en")

        speech.save(f"{directory}speech.mp4")

    def speak(self, directory):
        playsound(f"{directory}speech.mp4")
