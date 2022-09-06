# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:23:23 2022

@author: Marcin
"""

import pathlib
print (pathlib.Path.cwd())
print (pathlib.Path.home())

p = pathlib.Path('\home\evaluator\reports\2020\01\sales.csv')
print (p)

p = pathlib.Path ()
p = pathlib.Path.home() 
p= p/ 'reports/2020/01/sales.csv'

d= pathlib.Path.cwd() / 'reports/2020/01/sales.csv'
print (d)

from pathlib import Path


path1 = Path.home().joinpath('reports/2020/01/sales.csv')
path2 = Path.cwd().joinpath('reports/2020/01/sales.csv')
print(path1)
print(path2)

#%%
import pathlib

path = pathlib.Path.home() / 'reports/2020/01/sales.csv'

print (path)
print (path.parent)
print (path.name)
print (path.stem)
print (path.suffix)
print (path.parts)
#%%
from pathlib import Path

path = Path.home() / 'reports/2020/01/sales.csv'
for each in path.parents:
    print (each)
    
#%%
from pathlib import Path
path = pathlib.Path.home()/'reports'
path.is_dir()

print (path.is_dir())

# path.mkdir()(
# for each in sorted(Path.cwd().iterdir()):
#     print (each)
for each in path.parent.iterdir():
    print (each)

#%%
from collections import deque
from pathlib import Path

path = Path.cwd() / 'reports/ecommerce/2020/01'
parents = deque (path.parents)
parents.reverse()

for parent in parents:
    if not parent.is_dir():
        parent.mkdir()

path.mkdir()
print (path.is_dir())

#%%
from pathlib import Path


path = Path.cwd() / 'reports/ecommerce/2020/01'
path.mkdir(parents=True) #Tworzy wszystkie katalogi parent po drodze
print(path.is_dir())
#%%

from pathlib import Path
paths = [Path('C:/Users/Marcin/exercises/reports/2020/01'),
 Path('C:/Users/Marcin/exercises/reports/2020/02'),
 Path('C:/Users/Marcin/exercises/reports/2020/03'),
 Path('C:/Users/Marcin/exercises/reports/2020/04'),
 Path('C:/Users/Marcin/exercises/reports/2020/05'),
 Path('C:/Users/Marcin/exercises/reports/2020/06'),
 Path('C:/Users/Marcin/exercises/reports/2020/07'),
 Path('C:/Users/Marcin/exercises/reports/2020/08'),
 Path('C:/Users/Marcin/exercises/reports/2020/09'),
 Path('C:/Users/Marcin/exercises/reports/2020/10'),
 Path('C:/Users/Marcin/exercises/reports/2020/11'),
 Path('C:/Users/Marcin/exercises/reports/2020/12')]

# for path in paths:
    # path.mkdir(parents = True)

for each in path.parent.iterdir():
    print (each)

#%%
from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]

for path in paths:
    path.mkdir(parents=True)

for dir in sorted(path.parent.iterdir()):
    print(dir)    

#%%
from pathlib import Path
do_pliku = 'Open,High,Low,Close'
path = Path.cwd() / 'hello.txt'
if not path.is_file():
    with open (path, 'w') as file:
        file.write(do_pliku)

with open (path, 'r') as file:
    content = file.read()
    lines = file.readlines() # nie można jednoczenie dwóch operacji na treci pliku robić bo robi tylko pierwszą
    

print (content)
print (lines)
#%%

from pathlib import Path
path = Path.cwd() / 'hello.txt'
do_pliku = 'Open,High,Low,Close'
if not path.is_file():
    with open(path, 'w') as file:
        file.write(do_pliku)

with open(path, 'r') as file:
    content = file.read()
print(content)
#%%
from pathlib import Path
do_pliku = """Open,High,Low,Close'
            'asdas',
            'daasd'"""
path = Path.cwd() / 'hello.txt'

if not path.is_file():
    with open (path, 'w') as file:
        file.write(do_pliku)
        
content = path.read_text()# Bez otwierania pliku czyta...wow

print (content)
#%%
from pathlib import Path

path_dir = Path.cwd() / 'exercises/reports/2020/'

for i in range (0,13):
    path = path_dir / f'{str(i).zfill(2)}'
    path.mkdir(parents=True)
    
    
paths = path.parent.iterdir()
for each in paths:
    each_new = str(each) + '_sales'
    each.rename(each_new)

for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)
#%%
from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]

t = 3
targets = [Path.cwd() / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales' for i in range(t, t + 12)]
for target in targets:
    print(target)

#%%
from pathlib import Path
paths = [Path.cwd()/ f'exercises/media/music/playlist_{str(i).zfill(2)}' for i in range (1,11)]

print (paths)


# for path in paths:
    # path.mkdir(parents=True)
for dir in Path.cwd().joinpath('exercises/media/music').iterdir():
    print(dir)

#%%
from pathlib import Path
from pprint import pprint
import random
from gTTS import gTTS
extensions = ['.wav', '.mp3']

random.seed(42)
paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 7)]

# for path in paths:
#     path.mkdir(parents=True)

path_dict = dict()


# for path in paths:
#     path_file_list = []
#     for i in range (1,6):
#         path_extension = random.choice(extensions)
#         path_file = f'{str(i).zfill(2)}_music{path_extension}'
#         path_file_list.append(path_file)
#     path_dict[path]=path_file_list


paths_dict = {path: [f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}" 
                     for i in range(1, 6)] for path in paths}

fname_paths=[]
for key,values in path_dict.items():
    for value in values:
        fname_paths.append(key.joinpath(value))

# pprint (fname_paths)        


fname =























