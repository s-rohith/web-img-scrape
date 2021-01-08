import requests
from bs4 import BeautifulSoup
from collections import OrderedDict 
import json


result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, features="html.parser")

myDict = OrderedDict()

for h2_tags in soup.find_all("h2"):
    briefing = h2_tags.string
    a_tag = h2_tags.find("a")
    links = a_tag.attrs['href']
    myDict[briefing] = links

print(json.dumps(myDict, indent=4))