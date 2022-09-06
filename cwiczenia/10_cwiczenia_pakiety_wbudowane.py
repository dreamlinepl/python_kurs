# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:01:49 2022

@author: Marcin
"""

import calendar

yy = 2017
mm = 11
print(calendar.calendar(2020))

print (calendar.month(2020, 6))

#%%
import datetime 
data1= datetime.datetime(2020,6,1)
data2 = datetime.datetime(2020,7,18)
print (data2-data1)

from datetime import datetime
data1= datetime(2020,6,1)
data2 = datetime(2020,7,18)
print (data2-data1)

from datetime import date
data1= date(2020,6,1)
data2 = date(2020,7,18)
print (data2-data1)

#%%
import re 
string = 'Python 3.8'
string2 = '!@#$%^&45wc'
wynik = re.findall("\d", string) # znajduje cyfry
wynik2 = re.findall("\w", string2) # znajduje alfanumeryczne

print(wynik)
print(wynik2)
#%%
# Używając wbudowanego pakietu re do wyrażeń regularnych znajdź wszystkie 
# adresy email w podanym tekście:
import re    
raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"
wynik = re.findall("[\w\.-]+@[\w\.-]+", raw_text)
print(wynik)

#%%

import re    
text = 'Programowanie w języku Python - od A do Z'
wynik=text.split()

result = re.split(pattern=r"\s+", string=text)

print(result)
print(wynik)
#%%
import string
print(string.ascii_letters)
#%%
import collections
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
counter = collections.Counter(items)
print (counter)
#%%
import math
def sigmoid(x):
    return 1/(1+math.exp(-x))

print (sigmoid(sigmoid(5)))
#%%
import random
items = ['python', 'java', 'sql', 'c++', 'c']
random.seed(12)
idx = (random.randint(0, 5))
print (items[idx])

choice = random.choice(items)
print(choice)
#%%
import random
items = ['python', 'java', 'sql', 'c++', 'c']
random.seed(15)
random.shuffle(items)
print (items)
#%%
import pickle
ids = ['001', '003', '011']

with open('data.pickle', 'wb') as file:
    pickle.dump(ids, file)
#%%
import json
stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
with open ('stocks.json', 'w') as file:
    json.dump(stocks, file, sort_keys=True,indent=(4))
    





