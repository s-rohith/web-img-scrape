from bs4 import BeautifulSoup
import urllib.request
import requests
import os

# setting URL destination
url = "https://en.wikipedia.org/wiki/Vermilion_flycatcher"

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
images = soup.find_all("img", attrs={"class":"thumbimage"})

# Save location
root_path = os.getcwd()
image_path = root_path + '/scrapped-images/'
 
# downloading images
for image in images:
    print(image["src"])
    image_src = image["src"]
    scr_list = image_src.split('.')
    n = len(scr_list)
    file_ext = scr_list[n - 1]

    scr_list2 = image_src.split('%')
    new_scr_list2 = scr_list2[0].split('/')
    n2 = len(scr_list2[0].split('/')) - 1
    file_name = new_scr_list2[n2]

    os.chdir(image_path)
    urllib.request.urlretrieve("https:" + image_src, image_path + file_name + "." + file_ext)
