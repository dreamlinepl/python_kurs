# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:09:48 2022

@author: Marcin
"""

import sys
sys.version
print (sys.version.split(" ")[0])

#%%
import datetime

data1 = datetime.date(2021,1,1)
data2 = datetime.date(2021,7,31)
data3= datetime.date(1990,5,7)

print (data1)
print(data2)
print(data3)
#%%
import datetime

help(datetime.time)

# t1 = time(12,00,00)
# t2 = time(6,30,0)
# t3 = time(9,15,0)

# print (t1)
# print (t2)
# print (t3)

#%%
import datetime

# 2020-07-20 11:30:00
# 1990-03-10 12:00:00
# 2021-01-01 00:00:00

d1 = datetime.datetime(2020,7,20,11,30)
d2 = datetime.datetime(1990,3,10,12)
d3 = datetime.datetime(2021,1,1)
print (d1)
print (d2)
print (d3)
#%%
#Wykorzystując moduł wbudowany datetime wyznacz liczbę dni pomiędzy datami 2020-07-21 a 2020-12-31.
import datetime
d1 = datetime.date(2020,7,21)
d2 = datetime.date(2020,12,31)
diff = (d2 - d1).days

print(f'Number of days: {diff}')
#%%
#Wykorzystując moduł wbudowany datetime wyznacz dokładny czas jaki upłynął pomiędzy datami:
# 2020-07-20 11:30:00
# 2021-02-20 10:25:00

import datetime
d1 = datetime.datetime(2020,7,20,11,30)
d2 = datetime.datetime(2021,2,20,10,25)
diff = (d2 - d1)

print(f'{diff}')
#%%
# Wykorzystując moduł wbudowany datetime, klasę datetime oraz metodę strftime() dokonaj formatowania poniższej daty:
# 2021-04-20 11:30:00
# Na następujące formaty:
# 2021-04-20
# 20-04-2021
# 04-2021
# April-2021
# 20 April, 2021
# 2021-04-20 11:30:00
# 04/20/21 11:30:00
# 20(Tue) April 2021

import datetime
d1 = datetime.datetime(2021,4,20,11,30)

print (d1.strftime("%Y-%m-%d"))
print (d1.strftime("%d-%m-%Y"))
print (d1.strftime("%m-%Y"))
print (d1.strftime("%B-%Y"))
print (d1.strftime("%d %B, %Y"))
print (d1)
print (d1.strftime("%m/%d/%y %H:%M:%S"))
print (d1.strftime("%d(%a) %B %Y"))

#%%
#Wykorzystując moduł wbudowany datetime oraz funkcję strptime() dokonaj parsowania poniższych obiektów typu str:
date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'

import datetime

date1 = datetime.datetime.strptime(date_str_1, "%d %B %Y")
date2 = datetime .datetime.strptime(date_str_2, "%m/%d/%Y")
date3 = datetime .datetime.strptime(date_str_3, "%d-%m-%Y")
print (date1)
print (date2)
print (date3)
#%%
# Wykorzystując moduł wbudowany datetime wyznacz liczbę dni do końca obecnego roku.
import datetime
d1= datetime.datetime.now()
d2 = datetime.datetime(2022,12,31)
diff = d2-d1

today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
diff = (end_of_year - today)
print (f'Number of days until the end of the year:{diff.days}')

#%%
# Wykorzystując moduł wbudowany datetime wyznacz dokładny czas pozostały do końca obecnego roku.
import datetime
d1= datetime.datetime.now()
d2 = datetime.datetime(2022,12,31)
diff = d2-d1

print (f'Number of days until the end of the year:{diff}')

#%%
# Wykorzystując moduł wbudowany datetime oraz klasy date oraz timedelta z podanej daty 2020-01-01 00:00:00 otrzymaj datę:

# przesuniętą o 7 dni
# przesuniętą o 30 dni
# przesuniętą o 30 godzin
# przesuniętą o 15 minut
import datetime
data = datetime.datetime(2020,1,1)
data_7 = data + datetime.timedelta(7)
data_30 = data + datetime.timedelta(30)

data_30h = data + datetime.timedelta(hours=30)
data_15min = data + datetime.timedelta(minutes=15)

print (data_7)
print (data_30)
print (data_30h)
print (data_15min)

#%%

import datetime
start= datetime.datetime(2022,1,1)
dates =[]
nowa_data = start + datetime.timedelta(hours = 8)
for i in range (13):
    dates.append(nowa_data)
    nowa_data += datetime.timedelta(hours = 8)
    print (nowa_data)


dt = datetime.datetime(2020, 1, 1)
delta = datetime.timedelta(hours=8)

dates = [dt + i * delta for i in range(12)]

for date in dates:
    print(date)
#%%
# Wykorzystując moduł wbudowany datetime wyznacz wartość przyszłą (future value) kapitału 
# początkowego (present value) 1000 USD przy rocznej stopie procentowej 4% (rate) i 
# kapitalizacji złożonej dziennej odsetek zakładając czas trwania inwestycji od 2021-07-01 
# do 2021-12-31. Do obliczeń przyjmij, że rok ma 365 dni.
import datetime

pv = 1000
fv = float()
rate = 0.04
start = datetime.date(2021,7,1)
end = datetime.date(2021,12,31)
days= (end - start).days
rate = rate/365

fv = pv * (1+rate)**days
print (f'{fv:.2f}')

