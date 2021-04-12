import requests

class Miku():
    def __init__(self, url = "https://plushmiku.xyz/"):
        self.url = url
    def getRandomMiku(self):
        response = requests.get(self.url + "api/random")
        data = response.json()
        return data['username']
