# google_search.py
# - A script to do a google search
#   and return the results in text

from bs4 import BeautifulSoup
import requests

 # Google's CSS may change the class name so to
    # find the new one search through the html with:
    # with open('html_weather_results.txt', 'w') as f:
    #    f.write(s.prettify())

def googleSearch(search):
    url = f'https://www.google.com/search?&q={search}'
    page = requests.get(url)
    html = BeautifulSoup(page.text,"html.parser")
    return html

def get_webPage(url):
    