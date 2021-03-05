import requests
import shutil

from bs4 import BeautifulSoup


def multiplemikus(v):
    # = int(input("Specify how many mikus you want"))
    # count = 0
    basiclist = []
    for x in range(v):
        URL = "https://plushmiku.xyz"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.findAll("img")

        imscrape = results[0]
        URLEXT = imscrape.attrs["src"]

        fullurl = URL + URLEXT

        r = requests.get(fullurl, stream=True)
        string2 = ".jpg"

        filename = "miku" + str(x) + string2
        basiclist.append(filename)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            print("Website isn't up,can't help you there")

        # count = count + 1
    # numofelements = len(basiclist)
    return len(basiclist)
