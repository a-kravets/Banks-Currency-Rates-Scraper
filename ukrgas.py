
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import date
from datetime import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.ukrgasbank.com/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

data = soup.find_all('td', class_='val')

usd_buy = float(data[0].get_text())/100
usd_sell = float(data[1].get_text())/100
eur_buy = float(data[3].get_text())/100
eur_sell = float(data[4].get_text())/100


ukrgas = []
ukrgas.append(usd_buy)
ukrgas.append(usd_sell)
ukrgas.append(eur_buy)
ukrgas.append(eur_sell)
ukrgas.append(date.today().strftime('%Y-%m-%d'))
ukrgas.append(6)



