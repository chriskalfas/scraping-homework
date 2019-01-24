from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def init_browser():
    exec_path = {"exec_path": "C:\webdrivers\chromedriver"}
    return Browser("chrome",**exec_path, headless=False)

@staticmethod
def scrape():
    browser = init_browser()

    urls = ['https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest', 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars', 'https://twitter.com/marswxreport?lang=en', 'https://space-facts.com/mars/'] 
    for url in urls:
        response = requests.get(url)
        soup = bs(response.content, "html.parser")
    
    browser.visit(urls)

    news_latest = soup.title.text

    latest_p = soup.body.p.text

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    tables = pd.read_html(url)

    mars_data = {
        'news_latest': news_latest,
        'latest_p': latest_p,
        'mars_weather': mars_weather,
        'tables': tables
    }
    browser.quit()

return mars_data