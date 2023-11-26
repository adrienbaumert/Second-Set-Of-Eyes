# Second-Set-Of-Eyes

Copyright (C) 2023 Adrien Baumert

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

## Version
1.1.0

## Description

**Second-Set-Of-Eyes** is an open-source framework designed to assist blind and vision-impaired individuals in navigating their surroundings. With a core mission to empower developers, this framework can be leveraged to create robust applications or software tailored for the blind and vision-impaired community.

At its core, the functionality is simple so that no issues arise with vision impaired use: double-tap and it captures an image using `cv2`. This image is then processed through Salesforce's image captioning API, and the resulting description is made audible using Google's Text-to-Speech.

Emphasizing its open-source nature, Developers are invited to contribute, adapt, and implement this framework in diverse applications, pushing the boundaries of what's possible in accessibility technology.

## Features

- **Accessibility Framework**: The application effectively manages image capture, Salesforce image captioning API calls, and Google Text-To-Speech, to create a spoken description of a physical environment.
- **Interactive Demo**: The application is packaged with a demo to help developers visualize ways the framework can be utilized.
- **API Key Security**: The Hugging Face secret key is securely stored and accessed using a .env file, ensuring that sensitive information is not exposed.
- **GNU License**: The project is released under the GNU General Public License, granting users the freedom to use, study, share, and modify the software.

## Installation

1. Clone the repository:
```
git clone https://github.com/adrienbaumert/Second-Set-Of-Eyes
```

2. Install the required Python packages (Please read note below before installation):
```
pip install -r requirements.txt
```

3. Rename the `.env.template` file to `.env` and input your Hugging Face user access token
```
USER_ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Requirement Note

Please note that there are two requirements.txt files contained in this project. Installing the correct one is based on user needs. Installing the requirements.txt in the top level directory will install only the necessary packages for the framework. Installing the requirements.txt in the Demo folder will install all necessary packages to use the demo.

## Instructions to Find Hugging Face User Access Token
https://huggingface.co/docs/api-inference/quicktour

## Usage
To start an interactive text session, run `main.py` and follow the prompts in the console in the demo folder.

```bash
python main.py
```

## Debugging
If you encounter any issues, please reference the following:

**Ensure that your `.env` file is set up correctly:**
- User access token is valid
- User access token is added to the .env without quotes
- Image and speech directory are hardcoded with their absolute path
- Image and speech directory end with a /
- Image and speech directory are added without quotes

**Default camera:**

By default the camera is set in cv2 to camera 0. If this is set incorrectly the program may act in unstale ways. Experiment with different values if you are encountering errors.

This value is a constant located at the top PictureTaking.py:
```
# Setting camera:
CAMERA = 0
```

If you continue to encounter problems, please submit an issue on this repository.
