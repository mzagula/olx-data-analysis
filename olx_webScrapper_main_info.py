##########  Scraper through main list of announcements  ###############

import urllib.request
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

lsl=[]
col = ['title','price','location0','location1','location2','location3']
df=pd.DataFrame(columns=col)
headers = {'User-Agent': 'Mozilla/5.0'}

for j in range(1,69):
    link = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/?page="+str(j)
    r = requests.get(link, headers=headers)
    
    soup = BeautifulSoup(r.text, "html.parser")
    tr=soup.find_all('tr',class_='wrap')
    
    for i in tr:
        strong=i.find_all('strong')
        
        span=i.find_all('span')
        
        location0=span[0].text
        location1=span[1].text
        try: 
            location2=span[2].text
        except IndexError:
            location2=''

        try: 
            location3=span[3].text
        except IndexError:
            location3=''        
        
        title=strong[0].string
        price=strong[1].string
        
        lsl.append([title,price,location0, location1,location2,location3])

df=pd.DataFrame(lsl,columns=col)

df.to_csv('olx_mieszk_main_'+str(datetime.datetime.now().date())+'.csv')


