
import json
import requests
from datetime import date
from datetime import datetime


res = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    
if res.status_code != 200:
    raise Exception("ERROR: API request unsuccessful.")
    
data = res.json()

    
usd_buy = 0
usd_sell = 0
eur_buy = 0
eur_sell = 0  
    
for data_item in data:
    if data_item['ccy']=='USD' and data_item['base_ccy']=='UAH':
        usd_buy = data_item['buy']
        usd_sell = data_item['sale']
    if data_item['ccy']=='EUR' and data_item['base_ccy']=='UAH':
        eur_buy = data_item['buy']
        eur_sell = data_item['sale']


    
privat = []
privat.append(usd_buy)
privat.append(usd_sell)
privat.append(eur_buy)
privat.append(eur_sell)
privat.append(date.today().strftime('%Y-%m-%d'))
privat.append(3)
