# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:44:17 2022

@author: Marcin
"""

przedmioty = {'matematyka', 'polski'}
przedmioty.add('angielski')
print (przedmioty)
#%%
text = 'Programming in python.'
text = text.lower().replace(" ", "").replace(".", "")
letters = set(text)
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
consonants = letters - vowels

print ('Liczba elementów:', len(consonants))

consonants = letters.difference(vowels)
print(f'Liczba elementów: {len(consonants)}')
#%%
A = {2, 4, 6, 8}
B = {4, 10}

print ('Różnica symetryczna:', A.symmetric_difference(B))

sym_diff = A.symmetric_difference(B)
print(f'Różnica symetryczna: {sym_diff}')
#%%
ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
diff = ad1_id.symmetric_difference(ad2_id) 

print ('Wybrane ID:', diff)
#%%
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
bought = is_clicked.intersection(is_bought)
print(f'ID klientów: {bought}')
#%%
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')

print (wig20+mwig40)
#%%
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
result = (wig20,mwig40)
print (result)
#%%
members = (('Kasia', 23), ('Tomek', 19))
new_member = ('Adam', 26) 
members = (members[0], new_member, members[1])
print (members)

#%%
default = ('YES', 'NO', 'NO', 'YES', 'NO')
default.count('YES')
print (f"Liczba wystąpień: {default.count('YES')}")
#%%
names = ('Monika', 'Tomek', 'Adam', 'Olaf')
namesA =tuple(sorted(names))
print (namesA)

#%%
info = (('Monika', 19), ('Tomek', 21), ('Adam', 18))
namesA =tuple(sorted(info, reverse=True))
namesB =tuple(sorted(info))


print ('Rosnąco:', namesB)
print ('Malejąco:', namesA)

asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Rosnąco: {asc}')
print(f'Malejąco: {desc}')
#%%
stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
print (stocks[0][1][0])
#%%
cities = ['Warszawa', 'Łódź', 'Kraków']
cities.append('Gdańsk')
print (cities)
#%%
idx = ['001', '002', '001', '003', '001']
nb = idx.count('001')
print(f'Liczba wystąpień: {nb}')
#%%
text = 'Programowanie w języku Python'
text = text.lower().replace('ę', 'e').replace(' ', '')
lista = set (text)
sorted(lista)
print (sorted(lista)[:10])
#%%
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
nowa = ['phone.jpg'] + filenames
nowa.remove('ball.png')
print(nowa)

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)
#%%
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1 += day2
print (day1)

day1.extend(day2)
#%%
techs = ('python', 'java', 'sql', 'aws')

print (tuple(sorted (techs)))
#%%
hashtags = ['summer', 'time', 'vibes']
print(f'#{hashtags[0]}#{hashtags[1]}#{hashtags[2]}')

print('#' + '#'.join(hashtags))
#%%
capitals = {'Poland': 'Warsaw','Germany': 'Berlin', 'Austria':'Vienna'}
print (capitals)

print (capitals.keys())
print (capitals.values())
print (capitals.items())
print (capitals.get('Austria'))

#%%
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print (stocks.get('PLW'))
#print (stocks['PLW'])

print (stocks.get('TEN').get('Ten Square Games'))
print(stocks['TEN']['Ten Square Games'])

stocks['CDR']['CD Projekt'] = 310
print (stocks['CDR'])

stocks.update({'BBT' : {'Boombit': 23}})
#stocks['BBT'] = {'Boombit': 23}
print(stocks.values())

#%%

ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]
lista = dict()
for n in range (20):
    lista[n] = ticker[n]
print (lista)

print(list(enumerate(ticker)))
print(dict(enumerate(ticker)))
#%%
project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
lista = sorted(set(project_ids.values()))
print (lista)

result = list(set(project_ids.values()))
result.sort()
print(result)

#%%
stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
stats.pop('ruch')
print (stats)
# del stats['ruch']

#%%
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}

print(users.get('004', 'nieokreslony'))











