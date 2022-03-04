import pandas as pd
import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content
#site
#https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/366/santamaria-rs
#site = "https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/366/santamaria-rs"
#page = urllib2.urlopen(site)
#soup = BeautifulSoup(page)
#print soup.prettify()