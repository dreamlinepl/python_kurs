# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:48:29 2022

@author: Marcin
"""

filename = 'view.jpg'
rozszerzenie = filename[-3:]
print (rozszerzenie)
#%%
string = 'PKV-89415-PLN'
stringSTART = string [:3]
stringEND = string [-3:]
stringSHORT = stringSTART + stringEND
print (stringSHORT)

code = string[:3] + string[-3:]
print(code)
#%%

string = '1 0 0 1 0 1'
x = string.replace(" ","")
x = int (x, 2)
print (f'Znaleziona liczba:{x}')

#%%
text = 'Kurs Python'
print (text[::-1])
#%%
var1 = ''
var2 = ' '
var3 = '\n'

print (type (var1))
print (type (var2))
print (type (var3))
#%%
var1 = None
var2 = False
var3 = 'True'

print (type (var1))
print (type (var2))
print (type (var3))
#%%

flag = False

print(isinstance(flag, bool))

#%%
text = 'python jest popularnym językiem programowania.'

print (text.capitalize())

print(f"Liczba wystąpień: {text.count('p')}")

#%%
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
bool1 = code1[-4:] == "2020"
bool2 = code2[-4:] == "2020"

print(f'code1: {bool1}')
print(f'code2: {bool2}')

print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")
#%%
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

print(f"path1: {path1.startswith('youtube')}")
print(f"path2: {path2.startswith('youtube')}")
#%%
path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

print('path1:', path1.find('scientist'))
print('path2:', path2.find('scientist'))
print('path3:', path3.find('scientist'))

print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")
print(f"path3: {path3.find('scientist')}")
#%%

code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'

print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')
#%%
text = 'Google Colab'
print (text.lower())
print (text.upper())

#%%
text = '    Google Colab    '
print (text.rstrip())
print (text.lstrip())
print (text.strip())
#%%
code = 'FVNISJND-XX'
code.replace('-',' ')
print (code.replace('-',' '))
#%%
text = '340-23-245-235'
print (text.replace('-',''))
#%%
text = 'Open,High,Low,Close'
list = text.split(',')
print (list)
#%%
text = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny."""
list = text.split('\n')
print (list)
print(text.splitlines())
#%%
num = 34
print (str(num).zfill(6))
#%%
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'

numer = url[::-1].find('/')
url = url [-numer:]
print (url.replace('-',' '))

name = url.split('/')[-1]
name = name.replace('-', ' ')
print(name)
#%%







