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
print(f"Article Title: {title}")

author = soup.find("a", class_="gray-darkest b bb bc-gray bt-hover")
print(f"Article Author: {author.text}")

article_date = soup.find("span", class_="display-date gray-dark")
print(f"Article Date: {article_date.text}")

article_body = soup.find("div", class_="article-body")
# print(article_body.text)

print(f"{author.text} wrote \"{title}\" on {article_date.text}. The content of the article is as follows:\n{article_body.text}")
