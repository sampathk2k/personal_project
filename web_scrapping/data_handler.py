import sqlite3

DB_FILE = "scraped_data.db"

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, title TEXT, link TEXT)"""
    )
    conn.commit()
    conn.close()

def save_articles(articles):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for article in articles:
        cursor.execute("INSERT INTO articles (title, link) VALUES (?, ?)", (article["title"], article["link"]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()