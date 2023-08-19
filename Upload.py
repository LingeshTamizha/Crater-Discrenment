import os
import requests

# Set the URL of your backend
backend_url = "http://127.0.0.1:5000/"

# Path to the frames directory
frames_directory = "frames/"

# Iterate through each image file in the frames directory
def upload():
    for filename in os.listdir(frames_directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(frames_directory, filename)
            with open(image_path, "rb") as image_file:
                files = {'file': (filename, image_file, 'image/jpeg')}
                response = requests.post(backend_url, files=files)
                print(response.text)