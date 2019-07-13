from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import job_offer

lsl=[]
col=[]
headers= {'User-Agent':'Mozilla/5.0'}

main_link = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/'

r = requests.get(main_link, headers=headers)
col_otodom=['creator','localization','price','price_m3','title','size','type_of_building','building_material','rent',
            'year_of_constr','room_number','floor','window','stage','market','all_floor','heating','type_of_property', 
            'additional_info']
col_olx=['creator','localization','price','price_m3','title','size','type_of_building','market','type_of_creator']
df_OLX=pd.DataFrame(columns=col_olx)


r_main = requests.get(main_link, headers=headers)
soup_main = BeautifulSoup(r_main.text, "html.parser")
h3=soup_main.find_all('h3', attrs={"class":"lheight22 margintop5"})

all_offer=[]
all_offerOLX=[]
otodom_offer=[]
olx_offer=[]
id=1
column_set=[]
first_part=''
second_part=''

open('Detailed_mieszk_main_'+str(datetime.datetime.now().date()) + '.txt', 'w').close()

for i in h3:
    href=i.find('a')['href']

    r = requests.get(str(href), headers=headers)    
    soup = BeautifulSoup(r.text, "html.parser")

    re_olx=re.compile('https://www.olx.*')      
    re_otodom=re.compile('https://www.otodom.*')  
    
    s = job_offer.job_offer()
    s.set_link(href)

    if  'olx' in href:
        s.set_report("OLX")
    elif 'otodom' in href:
        s.set_report("OTODOM")

    if re_olx.match(href):
        div1=soup.find_all('div', attrs={"class":"clr descriptioncontent marginbott20"})
        if len(div1)==0:
            continue
        
        strong=div1[0].find_all('strong')
        tr=div1[0].find_all('tr')     
                        
        for i in range(0,13):
            
            try:
                first_part = tr[i].find('th').string
                second_part=tr[i].find('strong').text.replace('\t','').replace('\n','')
                               
                s.find_tagOLX(first_part,second_part)
                
            except TypeError or KeyError:
                pass
            except IndexError:
                pass   
            except AttributeError:
                pass  
        olx_offer.append(s.get_complete_list())
        print('OLX!')
    elif re_otodom.match(href):
        print('OTODOM!')
                
        div1=soup.find_all('div', attrs={"class":"css-1v9yl6n-AdOverview-className"})
        
        li=div1[0].find_all('li')

        x=''
        i=0
        otodom_offer=[]
        otodom_offer.append('otodom')
        while x=='':
            try:
                
                s.find_tagOTODOM(li[i].text)
            except IndexError:
                x='stop'
            
            i+=1
                       
    with open('Detailed_mieszk_main_'+str(datetime.datetime.now().date()) + '.txt', "a+", encoding="utf-8") as myfile:
        myfile.write(', '.join(s.get_complete_list()) + "\n")
     
       
    otodom_offer=[]
    olx_offer=[]
    
    id+=1
  