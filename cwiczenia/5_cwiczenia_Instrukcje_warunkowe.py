# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:27:46 2022

@author: Marcin
"""

filename = '01012020_sales.xlsx'

if filename.endswith('.xlsx'):
    print ('TAK')
else:
    print ('NIE')
#%%
code = 'DSVNDOICSN'

if code.isupper():
    print ('TAK')
else:
    print ('NIE')
#%%
number = 1.0
if isinstance(number, int):
    print ('TAK')
else:
    print ('NIE')
#%%
password = 'cskdnjcasa#sa!'
if len(password) >= 11 and password.find('!')>=1:
    print ('Hasło poprawne')
else:
    print ('Hasło niepoprawne')
    
    
password = 'cskdnjcasa#!'
if len(password) >= 11 and '!' in password:
    print('Hasło poprawne')
else:
    print('Hasło niepoprawne')
#%%
project_ids = ['02134', '24253']
project_id = '02135'
if not project_id in project_ids:   
    project_ids.append(project_id)

print (project_ids)
#%%
project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02'] == 'new':
    project_ids['02'] = 'open'

print (project_ids)
#%%
item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)

print (items)
#%%
text = ''

for i in range (10, 100):
    if i % 11 == 0 and i % 3 != 0:
        text = text + str(i) +","
text = text[:-1]
print (text)

result = []
for i in range(10, 100):
    if i % 11 == 0:
        result.append(str(i))
print(','.join(result))
#%%
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
        
print (result)
#%%
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
for item in items:
    if not item in result:
        result.append(item)
print (result)
#%%
text = 'Python jest bardzo popularnym językiem programowania'
text = text.lower().split(' ')
print(text[:4])

text = 'Python jest bardzo popularnym językiem programowania'
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)
#%%
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for item in probabilities:
    if item > 0.5:
        result.append(item)
print (result)
#%%
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for item in probabilities:
    if item >= 0.5:
        result.append(1)
    else:
        result.append(0)
print (result)
#%%
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = {'x':0, 'y':0, 'z':0}

for item in items:
    for key in result.keys():
        if item == key:
            result[key] += 1
print (result)

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1

print(freq)
#%%
text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
text = text.lower().replace('.','').replace(',','').replace('\n',' ')
lista = text.split(' ')
result = []
for word in lista:
    if len(word) > 10:
        result.append(word)
print (result)

words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 10]
print(words)
#%%
indexes = [
    'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 
    'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
    'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
    'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
    'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
    'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
    'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
    'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
]


for index in indexes:
    if '20' in index or '30' in index: 
        print (index)
#%%
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for key in gaming.keys():
    if gaming[key]>100.00:
        print (key)

for nazwa, cena in gaming.items():
    if cena > 100.0:
        print(nazwa)
#%%
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
for name in names:
    if name.isalpha():
        print(f'Hello {name}!')
#%%
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

for i in list1:
    if i in list2:
            print ("True")
            break
#%%
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True
for item in hashtags:
    if not isinstance(item, str):
        result = False

print (result)
#%%
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for key, info in gaming.items():
    if info[1] == 'USD':
        info[0] = info[0] * 4.0
        info[1] = 'PLN'

print (gaming)
#%%
names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for name in names:
    if not name.isalpha():
        continue
        print(name)
#%%
i=4
counter=2
result =['2','3']
while counter < 10:
    ma_dzielnik = False
    for dzielnik in range (2,i-1):
        if i % dzielnik == 0:
            break
    else:
        result.append(str(i))
        counter+=1
    i+=1

print(','.join(result))
#%%
# n - liczba okresów (w latach)
# pv - present value - wartość obecna
# r - stopa procentowa (roczna)
# fv - future value - wartość przyszła


pv = 1000
r = 0.04
n=0
fv = pv

while fv < 2 * pv:
    n+=1
    fv = fv*(1+r)
    
print (f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')

#%%
w_0 = -10
max_iters = 10000
iters = 0
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_0 - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1

print(f'Minimum lokalne w punkcie: {w_0:.2f}')
#%%

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
start = 0
end = len (numbers)
flag = False

while start<end:
    mid = (start+end) //2
    if numbers[mid] == target:
        flag = True
        break
    elif numbers[mid] < target:
        start =mid + 1
    else:
        end = mid- 1
if flag:
    print ('Znaleziono')
else:
    print ('Nie znaleziono')
#%%
suma = 3000
counter = 0
try: 
    result = suma/counter
    print (result)
except ZeroDivisionError:
    print('Dzielenie przez zero.')
#%%

try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print ('Nie znaleziono pliku.')
#%%
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'
try:
    print (users[user_id])
    
except KeyError:
    print('Klucz 004 nie występuje w słowniku. Dodawanie klucza...')
    users[user_id] = None

print (users)
























































