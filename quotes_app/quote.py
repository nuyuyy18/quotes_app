from bs4 import BeautifulSoup
import requests
from quote_scrap import trial
import pandas as pd


def get_HTML(url, is_dynamic):
    if is_dynamic == True:
        result = trial(url)
        return result
    else: 
        try:
            print(f"Fetching {url}...")
            response = requests.get(url, timeout=10)
            response.raise_for_status() 
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
        

def parse(html):
    page_quotes = []
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text_tag = quote.find('span', class_='text')
        author_tag = quote.find('small', class_='author')
        if text_tag and author_tag:
            text = text_tag.get_text()
            author = author_tag.get_text()
            dictionary = {
                "quote": text,
                "author": author
            }
            page_quotes.append(dictionary)
    return page_quotes

def main():
    urls = [f"https://quotes.toscrape.com/page/{i}/" for i in range(1, 11)] 
    print(len(urls), "URLs found.")

    i = len(urls) 
    page_quotes = []
    for index, url in enumerate(urls):
        print(f"Processing page {index + 1} of {i}: {url}")
        print(f"persentase: {(index + 1) / i * 100:.2f}%")  # Perbaikan persentase
        html = get_HTML(url, is_dynamic=True)
        if html is None:
            continue
        data = parse(html)
        page_quotes.extend(data)

    print(page_quotes) 
    print(f"Total quotes fetched: {len(page_quotes)}")
    return page_quotes

if __name__ == "__main__":
    main()
    