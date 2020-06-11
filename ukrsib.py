
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import date
from datetime import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://my.ukrsibbank.com/ua/personal/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

data_buy = soup.find_all('div', class_='rate__buy')
usd_buy = data_buy[0].p.get_text()
eur_buy = data_buy[1].p.get_text()

data_sell = soup.find_all('div', class_='rate__sale')
usd_sell = data_sell[0].p.get_text()
eur_sell = data_sell[1].p.get_text()



ukrsib = []
ukrsib.append(usd_buy)
ukrsib.append(usd_sell)
ukrsib.append(eur_buy)
ukrsib.append(eur_sell)
ukrsib.append(date.today().strftime('%Y-%m-%d'))
ukrsib.append(4)


