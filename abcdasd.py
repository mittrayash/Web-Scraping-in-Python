__author__ = 'mittr'

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import numpy as np

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-container"})

print(len(containers))

filename = "products.csv"
f = open(filename, "w")
headers = "Brand, Products, Shipping\n"
f.write(headers)

for container in containers:
    title_container = (container.div.div.img["title"])
    print("Brand = " + title_container)
    name = (container.findAll("a", {"class": "item-title"}))
    name_container = name[0].text
    print("Name = " + name_container)

    action = container.findAll("li", {"class": "price-ship"})
    shipping_container = action[0].text.strip()
    print("Shipping = " + shipping_container)
    print("\n")

    f.write(title_container + "," + name_container.replace(",", "|") + "," + shipping_container + "\n")
f.close();

