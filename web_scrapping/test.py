import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
titles = soup.find_all("a")
print(titles)
for title in titles:
    print(title.text)