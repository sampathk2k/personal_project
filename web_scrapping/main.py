from scraper import fetch_news
from data_handler import save_articles

# Run the scraping process manually
def scrape_and_store():
    articles = fetch_news()
    if articles:
        save_articles(articles)
        print("Data scraped & saved successfully!")
    else:
        print("failed")

# Execute once when running the script
if __name__ == "__main__":
    scrape_and_store()