import requests
from requests.auth import  HTTPBasicAuth

auth = ('admin','123456')
response = requests.get("https://github.com")
print(response.text)