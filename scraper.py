#scraper
#branch test

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site=site
    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html=r.read()
        print(html)
