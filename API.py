import requests

api_url = 'https://api.api-ninjas.com/v1/facedetect'
image_file_descriptor = open('IMG20220710140357.jpg', 'rb')
files = {'image': image_file_descriptor}
r = requests.post(api_url, files=files)
print(r.json())