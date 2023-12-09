"""
PLEASE READ:

The total number of valid proxies have been added from another file scrapped from the internet.
This program has 4 files in total (2 python, 2 text files to get proxies), however google form is not letting me add more than 1 file for submission of this project.
The proxy rotation can be better performed using online tools, however they are paid.
The solution is to scrap valid proxies off the internet, and then checking them for their actual validity.
In this current code we have gone through and actually used each of the valid proxies.
"""

import requests

with open("validproxy.txt", "r") as f:
    proxies = f.read().split("\n")

url = [
    "https://books.toscrape.com/",
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
]

counter = 0

for site in url:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(
            site, proxies={"http": proxies[counter], "http": proxies[counter]}
        )
        print(res.status_code)
        print(
            res.text
        )  # Comment this line if you need to see only the working proxy and not the HTML contents of the page
    except:
        print("Failed.")
    finally:
        counter += 1
        counter % len(proxies)  # Added incase the total number of proxies are less
