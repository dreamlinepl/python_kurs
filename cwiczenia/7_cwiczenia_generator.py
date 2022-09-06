# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:07:57 2022

@author: Marcin
"""

def file_gen(names):
    for name in names:
       if name.endswith('.txt'):
           yield name
    
fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
list(file_gen(fnames))
#%%

def enum(items:list()):
    i=0
    for item in items:
        tupla = (i, item)
        yield tupla
        i+=1
    
def enum2(items):
    idx = 0
    for item in items:
        yield (idx, item)
        idx += 1
    
print(list(enum(['TEN', 'CDR', 'BBT'])))
print(list(enum2(['TEN', 'CDR', 'BBT'])))
#%%
def dayname(idx):
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    yield days[idx-1]
    yield days[idx]
    yield days[idx+1]


for pair in dayname(0):
    print(pair)
#%%

