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
# File: ImageCaptioning.py
# Version : 1.0.0
# =================================================
# Importing necessary libraries
import requests
from dotenv import load_dotenv
import os

class ImageCaptioner:
    def __init__(self):
        # Loading .env file
        load_dotenv()

        # Setting a secret key constant to the value of the key
        # stored in the .env file
        self.SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

        # Setting the image captioning API and secret key
        self.API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        self.headers = {"Authorization": f"Bearer {self.SECRET_KEY}"}

    def query(self, filename):
        with open(filename, "rb") as file:
            data = file.read()
        response = requests.post(self.API_URL, headers=self.headers, data=data)

        text = response.json()[0]["generated_text"]

        return text
