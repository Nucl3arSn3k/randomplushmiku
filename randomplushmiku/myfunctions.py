import requests
import random

class Miku():
    def __init__(self, url = "https://plushmiku.xyz/"):
        self.url = url
        self.imageList = requests.get(self.url + "api/images.json").json()["images"]
    def getRandomMiku(self):
        return self.url + random.choice(self.imageList)[1:]
