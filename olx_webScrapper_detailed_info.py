from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import job_offer

headers= {'User-Agent':'Mozilla/5.0'}

main_link = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/'

r_main = requests.get(main_link, headers=headers)
soup_main = BeautifulSoup(r_main.text, "html.parser")
h3=soup_main.find_all('h3', attrs={"class":"lheight22 margintop5"})

id=1
first_part=''
second_part=''

col_list=['id','link','report','creator','level','isFurnished','numOfRooms','localization','price','price_m3',
              'title','size','type_of_building','market','type_of_creator','numOfLevels','material','finish','rent',
              'ownership','availability','windows','warming','year', 'description','offer_display','offer_added'
              ,'additional_info']

re_olx=re.compile('https://www.olx.*')      
re_otodom=re.compile('https://www.otodom.*')  
file_path = "C:\martaubuntu\olx_scraper\data"
file_name = '\Detailed_mieszk_main_'+str(datetime.datetime.now().date())
file_extension = "txt"
open(file_path +file_name + '.' + file_extension, 'w').close()

df = pd.DataFrame(columns=col_list)

for i in h3:
    href=i.find('a')['href']

    r = requests.get(str(href), headers=headers)    
    soup = BeautifulSoup(r.text, "html.parser")
   
    s = job_offer.job_offer()
    s.set_link(href)
    s.set_id(id)

    if  'olx.pl' in href:
        s.set_report("OLX")
    elif 'otodom.pl' in href:
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
            
        meta = soup.find('meta', attrs={"property":"og:description"})
        
        s.set_description(meta["content"])
        s.set_offer_display(soup.find_all('div', attrs={"class":"pdingtop10"})[1].strong.text)
        s.set_offer_added(soup.find('span', attrs={"class":"pdingleft10 brlefte5"}).text)
        s.set_localization(soup.find('span', attrs={"class":"block normal brkword"}).text)
        s.set_price(soup.find('strong', attrs={"class":"xxxx-large arranged"}))
      
        print('OLX!')
    elif re_otodom.match(href):
        print('OTODOM!')
                
        div1=soup.find_all('div', attrs={"class":"css-1v9yl6n-AdOverview-className"})
        
        li=div1[0].find_all('li')

        x=''
        i=0
        while x=='':
            try:
                
                s.find_tagOTODOM(li[i].text)
                s.set_localization(soup.find('a',attrs={"class":"css-1sulocs-baseStyle-Address-contentStyle"}))
                s.set_price(soup.find('div',attrs={"class":"css-1wko9rf-NavbarSticky-className css-8jxyhe-Price"}))
                s.set_additional_info(soup.find('div',attrs={"class":"css-qmf0ed-AdFeatures-className"}))

            except IndexError:
                x='stop'
            
            i+=1
                       
    with open(file_path +file_name + '.' + file_extension, "a+", encoding="utf-8") as myfile:
        myfile.write('; '.join(s.get_complete_list()) + "\n")
            
    id+=1   
    
  