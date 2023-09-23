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
