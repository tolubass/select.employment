from bs4 import BeautifulSoup
import requests
from csv import writer


url="https://www.naijaloaded.com.ng/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

