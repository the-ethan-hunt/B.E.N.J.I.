import requests
from bs4 import BeautifulSoup
import webbrowser

def lyric(link):
    link = '+'.join(link[1:])
    link = link.replace('+', ' ')
    title = link[1:]
    goog_search = "https://www.google.com/search?q=" + title + "+lyrics"
    r = requests.get(goog_search)
    soup = BeautifulSoup(r.text, "html.parser")
    webbrowser.open(soup.find('cite').text)
