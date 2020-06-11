
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import date
from datetime import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://alfabank.ua/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

usd_buy = soup.find(attrs={"data-currency": 'USD_BUY'}).get_text()
usd_sell = soup.find(attrs={"data-currency": 'USD_SALE'}).get_text()
eur_buy = soup.find(attrs={"data-currency": 'EUR_BUY'}).get_text()
eur_sell = soup.find(attrs={"data-currency": 'EUR_SALE'}).get_text()


alfa = []
alfa.append(usd_buy)
alfa.append(usd_sell)
alfa.append(eur_buy)
alfa.append(eur_sell)
alfa.append(date.today().strftime('%Y-%m-%d'))
alfa.append(2)

