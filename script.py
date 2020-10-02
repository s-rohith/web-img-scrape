# Scrape images from a website using BeautifulSoup
from bs4 import BeautifulSoup
import urllib.request
import requests
import os

# setting URL destination
url = "https://www.computerhistory.org/timeline/computers"

# retrieving HTML payload from the website
response = requests.get(url)

# checking response.status_code (if you get 502, try rerunning the code)
if response.status_code != 200:
    print(f"Status: {response.status_code} — Try rerunning the code\n")
else:
    print(f"Status: {response.status_code}\n")

# using BeautifulSoup to parse the response object
soup = BeautifulSoup(response.content, "html.parser")

# finding Post images in the soup
images = soup.find_all("img", attrs={"class":""})

# Save location
root_path = os.getcwd()
image_path = root_path + '/scrapped-images/'

# downloading images
number = 0
for image in images:
    print(image["src"])
    image_src = image["src"]
    
    li_src = image["src"].split('/')
    len_src =  len(li_src) - 1 
    file_name = li_src[len_src]

    urllib.request.urlretrieve("https:" + image_src, image_path + file_name)
    number += 1