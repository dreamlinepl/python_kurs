# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 04:49:46 2022

@author: Marcin
"""

import os

print (os.getcwd())

#listę o nazwie names zawierającą nazwy elementów w katalogu roboczym zaczynające się od litery 'e'. W odpowiedzi wydrukuj listę names do konsoli.
names = [name for name in os.listdir() if name.startswith('e')]
print (names)
#%%
# listę o nazwie names zawierającą posortowane alfabetycznie nazwy plików w katalogu roboczym z rozszerzeniem .py
names = sorted([name for name in os.listdir() if name.endswith('.py')])
print (names)
#%%
# w katalogu roboczym utwórz katalog o nazwie images. Następnie przejdź do katalogu images i wyświetl aktualną ścieżkę do katalogu roboczego.
# os.mkdir('images')
os.chdir('.\images') #Można też samo 'images'
print (os.getcwd())
#%%
current_dir = os.getcwd()
# os.chdir('..')
# os.mkdir('documents')
# os.chdir('documents')
# for i in range (13):
#     name = str(i) + '_sales'
#     if i<10: 
#         name = '0' + name
#     os.mkdir(name)
# print (sorted(os.listdir()))
os.mkdir('documents')
dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
for dirname in dirnames:
    path = os.path.join('documents', dirname)
    os.mkdir(path)

print(sorted(os.listdir('documents')))

#%%
import os
import random
base_dir = 'images'

if not os.path.exists(base_dir):
    os.mkdir(base_dir)

png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(png_dir):
    os.mkdir(png_dir)
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)
    
random.seed(30)
images = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]
   
    

for image in images:
    if image.endswith('.png'):
        open(os.path.join(png_dir, image), 'w').close()
    elif image.endswith('.jpg'):
        open(os.path.join(jpg_dir, image), 'w').close()

#%%      
for root, dirs, files in os.walk(base_dir):
    for file in files:
        print(file)
#%% 
fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
paths = [os.path.join(os.getcwd(), name) for name in fnames]
print (paths)
#%%
import os
fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
basic_dir = os.getcwd()
os.mkdir ('2020')
os.mkdir ('2021')

paths = [os.path.join(basic_dir, '2020',name) for name in fnames[:12]]
paths.append ([os.path.join(basic_dir, '2021', name) for name in fnames[12:]])

print (paths)
#%%
import os
basic_dir = os.getcwd()
fnames = [f'dir_{str(i).zfill(2)}' for i in range(1, 14)]
paths = [os.path.join(basic_dir,name) for name in fnames]
for path in paths:
    os.mkdir(path)
os.rmdir(os.path.join(basic_dir,'dir_13'))

#%%
for root, dirs, files in os.walk(basic_dir):
    for directory in dirs:
        if len(directory) == 6 and directory.startswith('dir'):
            print (directory)

fnames = [fname for fname in sorted(os.listdir()) if len(fname) == 6]
print(fnames)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    