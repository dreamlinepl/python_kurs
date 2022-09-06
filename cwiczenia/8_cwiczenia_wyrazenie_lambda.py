# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:25:04 2022

@author: Marcin
"""

stocks = ['playway', 'boombit', 'cd projekt']
length = list(map(len, stocks))
print (length)
#%%
def sort_list(items:tuple()):
    lista = sorted(items, key=lambda item: item[1])
    return lista

print (sort_list([(1, 3), (4, 1), (4, 2), (0, 7)]))
print (sort_list([('a', 'b'), ('g', 'a'), ('z', 'd')]))
#%%
def func_1(x, y):
    return x + y + 2

func_2 = lambda x,y: x + y + 2
    
print (func_2(2,3))
#%%
items = [(3, 4), (2, 5), (1, 4), (6, 1)]
items.sort(key=lambda item: item[0]**2 + item[1]**2)
lista = sorted(items, key=lambda item: item[0]**2 + item[1]**2)
print(items)
print(lista)
#%%
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

# stocks=sorted(stocks, key=lambda stock: stock['price'])
# print (stocks)
# stocks.sort(key=lambda stock:stock['name'])
# print (stocks)


lista = list(filter(lambda item: item['indeks'] == 'mWIG40',stocks))
lista = list(sorted(stocks, key=lambda stock: stock['name']))
print (lista)

#%%
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

stocks_bool = list(map(lambda stock: stock['indeks']=='mWIG40', stocks))

print(stocks_bool)
#%%
items = ['P-1', 'R-2', 'D-4', 'F-6']
items = list(map(lambda item:item.replace('-',''), items))

print (items)
#%%
num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]
items = list(map( lambda num1,num2: num1%num2, num1, num2 ))

print (items)
#%%































































