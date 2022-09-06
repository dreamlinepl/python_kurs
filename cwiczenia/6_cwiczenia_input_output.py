# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:28:28 2022

@author: Marcin
"""


lines =[]
with open('playway.txt', 'r') as file:
    for line in file:
            lines.append (line.split(","))

licznik = 0
suma = float()
for i in range (1,len(lines)):
    suma += float(lines[i][4])
    licznik += 1
srednia = suma/ licznik


print (f"3-dniowa rednia cena zamknięcia: {srednia:.2f}")

with open('playway.txt', 'r') as file:
     lines = file.readlines()

close = []

for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))

close_avg = sum(close) / len(close)
print(f'3-dniowa średnia cena zamknięcia: {close_avg:.2f}')
#%%
lines =[]
with open('indexy.txt', 'r') as file:
     lines = file.read().splitlines()
close = []
lista = []
for line in lines:
    if line.startswith("WIG"):
        lista.append(line)
    
print (lista)

with open('indexy.txt', 'r') as file:
     lines = file.read().splitlines()

indexes = [index for index in lines if index.startswith('WIG')]
print(indexes)

#%%

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
close = []
data = list()
zamkniecie = list() 

for idx, line in enumerate(content):
    if idx> 0:
        line = line.split(",")
        data.append(line[0])
        zamkniecie.append(float(line[4]))

slownik = {'Data': data, 'Zamkniecie': zamkniecie}


data = [(line.split(',')[0], line.split(',')[4]) for line in content]
print (data)
# result = {
#     data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
#     data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
#     }
# print(result)
#%%

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
close = []

data = [int(line.split(',')[5]) for line in content[1:]]

max_vol = max(data)

volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(vol) for vol in volumes]

max_vol = max(volumes)
print(f'Max Vol: {max_vol}')
#%%
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
close = []

data = [line.split(',')[0] for line in content[1:]]
volume = [int(line.split(',')[-1]) for line in content[1:]]

data_for_max_volume = data [volume.index(max(volume))]

print(f'Data for max volume: {data_for_max_volume}')


with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0], int(val[1])) for val in data]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Data: {max_date}')

#%%
parzyste = [i for i in range(2,20)][::2]

with open('num.txt', 'w') as file:
    for i in parzyste:
        print(i, file=file)
#%%
numbers = list(range(1, 20))
even = [num for num in numbers if num % 2 == 0]

with open('num.txt', 'w') as file:
    for num in even:
        file.write(str(num) + '\n')
#%%
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)
#%%
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')












































