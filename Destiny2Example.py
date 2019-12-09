import requests
from bs4 import BeautifulSoup

URL = 'https://store.steampowered.com/app/1085660/Destiny_2/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find("div", class_="apphub_AppName").getText().strip()
price = soup.find("div", class_="game_purchase_price price").getText().strip()

print(title)
print(price)
