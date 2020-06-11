
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import date
from datetime import datetime

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.aval.ua/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


aval_usd_rate = soup.find('div', 'rate-numbers-usd', 'span').get_text().split()
aval_eur_rate = soup.find('div', 'rate-numbers-eur', 'span').get_text().split()
aval_rub_rate = soup.find('div', 'rate-numbers-rub', 'span').get_text().split()

aval = []
aval.append(aval_usd_rate[0])
aval.append(aval_usd_rate[1])
aval.append(aval_eur_rate[0])
aval.append(aval_eur_rate[1])
aval.append(date.today().strftime('%Y-%m-%d'))
aval.append(1)

