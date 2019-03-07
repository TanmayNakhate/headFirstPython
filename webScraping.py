from bs4 import BeautifulSoup
import requests
import sys

url = "http://www.imbd.com/chart/top"
response = requests.get(url)
soup =BeautifulSoup(response.text)
print(soup)

