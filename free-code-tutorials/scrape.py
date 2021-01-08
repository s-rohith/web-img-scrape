import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com")
print(result.status_code)
# print(result.headers)

src = result.content
# print(src)

soup = BeautifulSoup(src, features="html.parser")
links = soup.find_all("a")

for link in links:
    print(link.attrs['href'])
