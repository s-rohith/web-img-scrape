import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, features="html.parser")

urls = []
for h2_tags in soup.find_all("h2"):
    a_tag = h2_tags.find("a")
    links = a_tag.attrs['href']
    urls.append(links)

print(urls)
