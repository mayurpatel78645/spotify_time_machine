import requests
from bs4 import BeautifulSoup

bollywood_url = "https://www.bbc.co.uk/asiannetwork/vote/top-songs/"
hollywood_url = "https://www.billboard.com/charts/hot-100/2016-07-02/"
urls = [bollywood_url, hollywood_url]


def scrape(url):
    request = requests.get(url)
    response = request.text
    soup = BeautifulSoup(response, "html.parser")
    if "billboard" in url:
        titles = [song.getText().strip() for song in soup.select("h3") if ":" not in song.getText()][3:103]
    else:
        titles = [song.getText() for song in soup.select(".intro") if "-" in song.getText()][1:]
    return titles


def create_txt_file(file_name, url):
    bollywood_titles = scrape(url)
    with open(f"{file_name}.txt", "w") as file:
        for title in bollywood_titles:
            file.write(f"{title}\n")


for url in urls:
    create_txt_file("hollywood" if "billboard" in url else "bollywood", url)
