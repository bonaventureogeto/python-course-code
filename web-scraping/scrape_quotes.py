# web scraping - pulling data from websites
# robots.txt
# https://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
import csv


def scrape(pages):
    """ quotes website scraper """
    headers = {"User-agent": "Mozilla/5.0"}
    base_url = "https://quotes.toscrape.com/page/{}/"

    # open CSV
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])

        for i in range(1, pages + 1):
            url = base_url.format(i)
            # fetch and parse
            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            quotes = soup.find_all("div", class_="quote")

            # extract and write rows
            for quote in quotes:
                text = quote.find("span", class_="text").get_text()
                author = quote.find("small", class_="author").get_text()
                tags = [t.get_text()
                        for t in quote.find_all("a", class_="tag")]
                tags_str = ','.join(tags)
                writer.writerow([text, author, tags_str])

    print("DONE!")


scrape(10)
