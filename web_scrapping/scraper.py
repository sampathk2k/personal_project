import requests
from bs4 import BeautifulSoup

URL = "https://www.carwale.com/bmw-cars/"

def fetch_news():
    response = requests.get(URL)
    if response.status_code != 200:
        return []
    else:
        print("failed")
    soup = BeautifulSoup(response.text, "html.parser")
    #articles = soup.find_all("a", class_="storylink")
    articles = soup.find_all("a")
    print([{"title": article.text, "link": article["href"]} for article in articles])

    return [{"title": article.text, "link": article["href"]} for article in articles]

if __name__ == "__main__":
    print(fetch_news())