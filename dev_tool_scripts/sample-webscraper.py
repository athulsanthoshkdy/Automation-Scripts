import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h1')
        
        for title in titles:
            print(title.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

url = input("Enter the URL to scrape titles from: ")
scrape_titles(url)
