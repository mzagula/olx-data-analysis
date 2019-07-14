# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:48:28 2019

@author: Marta
"""

class job_offer:
    import re
          
    def __init__(self):
        self.id = ""
        self.report = ""
        self.link = ""
        self.creator = ""
        self.level = ""
        self.isFurnished = ""
        self.numOfRooms = ""
        self.localization = ""
        self.price = ""
        self.price_m3 = ""
        self.title = ""
        self.size = ""
        self.type_of_building = ""
        self.market = ""
        self.type_of_creator = ""
        self.numOfLevels = ""
        self.material = ""
        self.warming = ""
        self.windows = ""
        self.year = ""
        self.finish = ""
        self.rent = ""
        self.ownership = ""
        self.availability = ""
        self.windows = ""
        self.warming = ""
        self.description = ""
        self.offer_display = ""
        self.offer_added = ""
        self.additional_info = ""
        
    def set_id(self,value):
        self.id=str(value)
        
    def get_id(self):
        return self.id

    def set_report(self,value):
        self.report=value
        
    def get_report(self):
        return self.report

    def set_link(self,value):
        self.link=value
        
    def get_link(self):
        return self.link

    def set_creator(self,value):
        self.creator=value
        
    def get_creator(self):
        return self.creator
 
    def set_level(self,value):
        self.level=value
        
    def get_level(self):
        return self.level
    
    def set_isFurnished(self,value):
        self.isFurnished=value
        
    def get_isFurnished(self):
        return self.isFurnished
      
    def set_localization(self,value):
        self.localization=value.replace('\n','').replace('\r','').replace('\t','')
       
    def get_localization(self):
        return self.localization
        
    def set_price(self,value):
        self.price=value
       
    def get_price(self):
        return self.price
    
    def set_price_m3(self,value):
        self.price_m3=value
       
    def get_price_m3(self):
        return self.price_m3
    
    def set_title(self,value):
        self.title=value
       
    def get_title(self):
        return self.title
    
    def set_size(self,value):
        self.size=value
       
    def get_size(self):
        return self.size
    
    def set_type_of_building(self,value):
        self.type_of_building=value
       
    def get_type_of_building(self):
        return self.type_of_building
    
    def set_market(self,value):
        self.market=value
       
    def get_market(self):
        return self.market
    
    def set_type_of_creator(self,value):
        self.type_of_creator=value
       
    def get_type_of_creator(self):
        return self.type_of_creator

    def set_numOfRooms(self,value):
        self.numOfRooms=value
       
    def get_numOfRooms(self):
        return self.numOfRooms  
    
    def set_numOfLevels(self,value):
        self.numOfLevels=value
       
    def get_numOfLevels(self):
        return self.numOfLevels

    def set_material(self,value):
        self.material=value
       
    def get_material(self):
        return self.material  
    
    def set_finish(self,value):
        self.finish=value
       
    def get_finish(self):
        return self.finish  
    
    def set_rent(self,value):
        self.rent=value
       
    def get_rent(self):
        return self.rent  
    
    def set_ownership(self,value):
        self.ownership=value
       
    def get_ownership(self):
        return self.ownership  

    def set_availability(self,value):
        self.availability=value
       
    def get_availability(self):
        return self.availability  

    def set_windows(self,value):
        self.windows=value
       
    def get_windows(self):
        return self.windows  
    
    def set_warming(self,value):
        self.warming=value
       
    def get_warming(self):
        return self.warming  

    
    def set_year(self,value):
        self.year=value
       
    def get_year(self):
        return self.year  
 
    
    def set_additional_info(self,value):
        self.additional_info=value
       
    def get_additional_info(self):
        return self.additional_info
    
    def set_description(self,value):
        self.description=value.replace('\n','').replace('\r','').replace(';',',')
       
    def get_description(self):
        return self.description  
    
    def set_offer_display(self,value):
        self.offer_display=value
       
    def get_offer_display(self):
        return self.offer_display  


    def set_offer_added(self,value):
        self.offer_added=value.replace('\n','').replace('\r','').replace('\t','')
       
    def get_offer_added(self):
        return self.offer_added
    
    def get_complete_list(self):
        list=[self.id,self.link,self.report,self.creator,self.level,self.isFurnished,self.numOfRooms,
              self.localization,self.price,self.price_m3,self.title,self.size,
              self.type_of_building,self.market,self.type_of_creator, self.numOfLevels,
              self.material,self.finish, self.rent,self.ownership, self.availability,
              self.windows,self.warming,self.year,self.description,self.offer_display,
              self.offer_added,self.additional_info]
        return list       
            
    def find_tagOLX(self,first_part, second_part):
        if(first_part == "Oferta od"):
            self.set_creator(second_part)
        elif(first_part == "Cena za m²"):
            self.set_price_m3(second_part)          
        elif(first_part == "Poziom"):
            self.set_level(second_part)   
        elif(first_part == "Umeblowane"):
            self.set_isFurnished(second_part)               
        elif(first_part == "Rynek"):
            self.set_market(second_part)  
        elif(first_part == "Powierzchnia"):
            self.set_size(second_part)              
        elif(first_part == "Liczba pokoi"):
            self.set_numOfRooms(second_part)    
                       
    def extractData(value):
        value[value.index(':')+1:].strip()  
            
    def find_tagOTODOM(self, value):
        
        if('Powierzchnia:' in value):            
            self.set_size(value[value.index(':')+1:].strip() )
        
        elif('Liczba pokoi:' in value):
            self.set_numOfRooms(value[value.index(':')+1:].strip())

        elif('Rynek:' in value):
            self.set_market(value[value.index(':')+1:].strip())
            
        elif('Rodzaj zabudowy:' in value):
            self.set_type_of_building(value[value.index(':')+1:].strip())

        elif('Piętro:' in value):
            self.set_level(value[value.index(':')+1:].strip())

        elif('Liczba pięter:' in value):
            self.set_numOfLevels(value[value.index(':')+1:].strip())
            
        elif('Materiał budynku:' in value):
            self.set_material(value[value.index(':')+1:].strip())

        elif('Okna:' in value):
            self.set_windows(value[value.index(':')+1:].strip())

        elif('Ogrzewanie:' in value):
            self.set_warming(value[value.index(':')+1:].strip())

        elif('Rok budowy:' in value):
            self.set_year(value[value.index(':')+1:].strip())

        elif('Stan wykończenia:' in value):
            self.set_finish(value[value.index(':')+1:].strip())

        elif('Czynsz:' in value):
            self.set_rent(value[value.index(':')+1:].strip())

        elif('Forma własności:' in value):
            self.set_ownership(value[value.index(':')+1:].strip())

        elif('Dostępne od:' in value):
            self.set_availability(value[value.index(':')+1:].strip())

        else:
            print('Brak!')
            print(value)
            
            
