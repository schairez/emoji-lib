__author__ = "Sergio Chairez"


import json
import requests
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
# from typing import Union


FULL_EMOJI_LIST_URL = "http://unicode.org/emoji/charts-13.0/full-emoji-list.html#1f3f4_e0067_e0062_e0073_e0063_e0074_e007f"


# urllib version
def get_emoji_html_data(url: str) -> str:
    req = urllib.request.Request(FULL_EMOJI_LIST_URL)
    with urllib.request.urlopen(req) as response:
        try:
            req_html_str = response.read().decode("UTF-8")
            return req_html_str

        except urllib.error.URLError as e:
            raise e


# requests version
def req_emoji_html_data(url: str) -> str:
    return_request = requests.get(url)
    try:
        return_request = requests.get(url)
        if return_request.status_code == 503:
            return_request.raise_for_status()

        return return_request.text

    except requests.exceptions.HTTPError:
        print("ERROR", return_request.status_code)


def wrangle_emoji_html_soup(html_data: str):
    soup = BeautifulSoup(html_data, "html.parser")
    # l_data = []
    d = {}
    for row in soup.find_all("tr"):
        # go to next loop iteration if th tag in tr
        if row.find("th"):
            continue

        emoji_glyph = row.find("td", attrs={"class": "chars"}).text
        short_name = row.find(
            "td", attrs={"class": "name"}).text.replace('"', '')
        unicode_code_point = row.find("td", attrs={"class": "code"}).text
        d[short_name] = emoji_glyph

    return d


if __name__ == "__main__":
    d = wrangle_emoji_html_soup(req_emoji_html_data(FULL_EMOJI_LIST_URL))
    print(d['farmer'])
