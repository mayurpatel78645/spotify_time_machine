import requests
from bs4 import BeautifulSoup


class WebScraper:
    @staticmethod
    def scrape(url):
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        if "billboard" in url:
            titles = [song.getText().strip() for song in soup.select("h3") if ":" not in song.getText()][3:103]
        else:
            titles = [song.getText() for song in soup.select(".intro") if "-" in song.getText()][1:]
        return titles
