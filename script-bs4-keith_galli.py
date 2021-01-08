import requests
from bs4 import BeautifulSoup as bs

line = "\n--------------------------------------------------------\n"

#### FIND AND FIND ALL METHOD

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
# r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = bs(r.content, features="html.parser")
# print(soup)

# first_header = soup.find("h2")
# first_header = soup.find_all("h2")
first_header = soup.find_all(["h1", "h2"])
# print(first_header, line)

paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# print(paragraph, line)

body = soup.find("body")
div = body.find("div")
header = div.find("h1")
# print(body, line, div, line, header)

# search_string = soup.find_all("p", string="Some")
import re
paragraphs = soup.find_all("p", string=re.compile("Some"))
# print(paragraphs)

headers = soup.find_all("h2", string=re.compile("(H|h)eader"))
# print(headers)

#### SELECT METHOD
content = soup.select("div p")
# print(content)

paragraphs = soup.select("h2 ~ p")
print(paragraphs)