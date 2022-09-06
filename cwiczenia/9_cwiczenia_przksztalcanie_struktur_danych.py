# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:00:44 2022

@author: Marcin
"""

omega = [(i, j) for i in range(1, 7) for j in range(1, 7)]
print (omega)
sum_gt_10 = list()
for pair in omega:
    sum = pair[0]+pair[1]
    if  sum>10:
        sum_gt_10.append(sum)

print(sum_gt_10)
# sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}

print(f'P-stwo: {len(sum_gt_10) / len(omega):.2f}')

#%%
desc = "Playway: Playway to producent gier komputerowych."
desc = desc.lower().replace(".","").replace(":", "")
desc = set(desc.split())
print(len (desc))

desc = "Playway: Playway to producent gier komputerowych."
word_list = desc.lower().replace(':', '').replace('.', '').split()
word_unique = set(word_list)
print(len(word_unique))
#%%
omega = [(i, j) for i in range(1, 7) for j in range(1, 7)]


sum_gt_45 = {pair for pair in omega if pair[0]**2 + pair[1]**2>=45}
sum_gt_45_2 = {(x, y) for x, y in omega if x**2 + y**2 >= 45}


print(f'P-stwo: {len(sum_gt_45_2) / len(omega):.2f}')
#%%
# Rozważmy trzykrotny rzut kostką. Zbuduj przestrzeń zdarzeń elementarnych omega, 
# następnie policz prawdopodobieństwo uzyskania trójki, której suma jest 
# podzielna przez 7. Wykorzystaj set comprehension. Wynik zaokrąglij do 
# drugiego miejsca po przecinku.

omega = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
sum_gt_7 ={(x,y,z) for x,y,z, in omega if (x+y+z) % 7 == 0}
print(sum_gt_7)
print(f'P-stwo: {len(sum_gt_7) / len(omega):.2f}')
#%%

# Oblicz prawdopodobieństwo tego, że w trzech rzutach symetryczną sześcienną 
# kostką do gry suma kwadratów liczb uzyskanych oczek będzie podzielna przez 3. 
# Wykorzystaj set comprehension. Wynik zaokrąglij do czwartego miejsca po 
# przecinku.

omega = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
sum_gt_3 ={(x,y,z) for x,y,z, in omega if (x**2 + y**2 + z**2) % 3 == 0}
print(sum_gt_3)
print(f'P-stwo: {len(sum_gt_3) / len(omega):.4f}')
#%%
# Rzucamy trzykrotnie symetryczną kostką sześcienną do gry. 
# Oblicz prawdopodobieństwo zdarzenia:

# A – na każdej kostce wypadnie nieparzysta liczba oczek
# Wykorzystaj set comprehension. Wynik zaokrąglij do trzeciego 
# miejsca po przecinku.

omega = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
sum_gt_even ={(x,y,z) for x,y,z, in omega if x%2!=0 and y%2!=0 and z%2!=0}
print(sum_gt_even)
print(f'P-stwo: {len(sum_gt_even) / len(omega):.4f}')

#%%
with open('gaming.txt','r') as file:
    text = file.readlines()
close = []
new_text = []
for each in text:
    if each != ("\n"):
        if each.endswith("\n"):
            new_text.append(each.replace('\n', ""))
print (new_text)

text = [line.replace('\n', '') for line in text]
text = [line for line in text if len(line) > 0]
print(text)
#%%
# Używając list comprehension policz cenę brutto dla każdego produktu. 
# Cenę zaokrąglij do drugiego miejsca po przecinku. Otrzymaną listę wydrukuj 
# do konsoli.

net_price = [5.5, 4.0, 9.0, 10.0]
tax = 0.23

brutto = list(map(lambda item:round(item*(tax+1),2), net_price))
gross_price = [round(price * (1 + tax), 2) for price in net_price]
print(brutto)
#%%
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
fv = [round(pv*(1+r)**n,2) for r in rate]
print (fv)
#%%
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
rv = [round(pv*(1+r)**n-pv,2) for r in rate]
print (rv)
#%%
with open('plw.txt', 'r') as file:
    lines = file.read().splitlines()
close = []

lines = [line.split() for line in lines if line !=""]

print (lines)
#%%
# 1. Zamień duże litery na małe.
# 2. Usuń przecinki oraz kropki.
# 3. Podziel tekst na tokeny/wyrazy względem spacji.
# 4. Pozostaw tylko wyrazy mające minimum 8 znaków.
# 5. Posortuj wyrazy alfabetycznie.
# Wynik wydrukuj do konsoli.

with open('plw.txt', 'r') as file:
    lines = file.read()
close = []
word_list = lines.lower().replace(",", "").replace(".", "").split()
word_above_8 = [word for word in word_list if len(word) >= 8]
word_above_8.sort()
print (word_above_8)

#%%
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
data_new = []
for key, value in data.items():
    data_new.append([key, value])

data_new = [[key,value] for key, value in data.items()]
print (data_new)
#%%
# Wykorzystując dict comprehension utwórz słownik, który zmapuje liczby od 1 do 7
#  na ich kwadraty.

result = {i:i**2 for i in range(1, 8)}
print(result)
#%%
# Wykorzystując dict comprehension zbuduj słownik, który zmapuje nazwy spółek na 
# liczbę znaków w jej nazwie. Wynik wydrukuj do konsoli.
stocks = ['Playway', 'CD Projekt', 'Boombit']
result = {stock:len(stock) for stock in stocks}
print (result)
#%%
#Używając dict comprehension przestaw wartości z kluczami. 
# Wynik wydrukuj do konsoli.
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
result = {value:key for key,value in stocks.items()}
print (result)
#%%
# Wykorzystując dict comprehension wydobądź ze słownika pary 
# klucz:wartość o wartości powyżej 100. Wynik wydrukuj do konsoli.
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {key:value for key, value in stocks.items() if value >100}
print (result)
#%%
#Zbuduj listę składającą się ze słowników mapujących kolejne cyfry od 
# 1 do 9 włącznie na ich odpowiednie k-te potęgi, dla k = 1, 2, 3.
numbers = [i for i in range(1,10)]
potegi = [k for k in range(1,4)]
result = [{i:i**k for i in numbers} for k in potegi]

data = [{i: i**j for i in range(1, 10)} for j in range(1, 4)]
print(result)
print (data)
#%%
indeksy = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']
x ={}
data = {}
for indeks in indeksy:
    for properity in properties:
        x.update({properity:None})
        data.update({indeks : x})

data = {indeks:{properity:None for properity in properties} for indeks in indeksy}
print (data)

#%%
indeksy = ['WIG20', 'mWIG40', 'sWIG80']
data = {i:indeks for i in range (0, len(indeksy)) for indeks in indeksy}
data = {key: val for key, val in enumerate(indeks)}
print (data)































































