import requests
from bs4 import BeautifulSoup

bollywood_url = "https://www.bbc.co.uk/asiannetwork/vote/top-songs/"

request = requests.get(bollywood_url)
response = request.text
soup = BeautifulSoup(response, "html.parser")

bollywood_titles = [title.getText() for title in soup.select(".intro") if "-" in title.getText()][1:]

for title in bollywood_titles:
    print(title)
