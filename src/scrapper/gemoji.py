__author__ = "Sergio Chairez"


import json
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(
        "https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json")
    with urllib.request.urlopen(req) as response:
        js = json.loads(response.read())

    for i in js[:10]:
        print(i['emoji'], i['aliases'][0])
