import requests 
from lxml import etree
from bs4 import BeautifulSoup

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
page = requests.get(url)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

## Use XPath 
dom = etree.HTML(str(soup))
title = dom.xpath('//*[@id="main-content"]/span')[0].text
print(title)

article_body = soup.find("div", class_="article-body")
print(article_body.text)
# print(article_body.prettify())
