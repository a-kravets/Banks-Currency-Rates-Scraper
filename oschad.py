
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import date
from datetime import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.oschadbank.ua/ua'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

usd_buy = soup.find('strong', class_='buy-USD').get_text()
usd_sell = soup.find('strong', class_='sell-USD').get_text()
eur_buy = soup.find('strong', class_='buy-EUR').get_text()
eur_sell = soup.find('strong', class_='sell-EUR').get_text()


oschad = []
oschad.append(usd_buy)
oschad.append(usd_sell)
oschad.append(eur_buy)
oschad.append(eur_sell)
oschad.append(date.today().strftime('%Y-%m-%d'))
oschad.append(5)

