# -*- coding: utf-8 -*'-
"""
Created on Tue Mar 15 18:39:51 2022

@author: Marcin
"""
print ('Ucz się Pythona!')
#%%
age = 20
print('Mam', age, 'lat')
print ('Mam {} lat'.format(age))
print (f'Mam {age} lat')
#%%
jezyk ='Python'
wersja = 3.8

print (f'Uczę się języka {jezyk} w wersji {wersja}')
#%%
cena = 199.99


print (f'Towar kosztuje {cena}.')
print ('Towar kosztuje', cena)
#%%
cena = 69.99
print (f'Towar kosztuje {cena}.')
#%%
cena = 34.99
waga = 10

print (f'Cena: {cena} PLN. Waga: {waga} kg')
#%%
pi = 3.1415926535
round_pi = round(pi,2)

print (f'Przybliżenie liczby pi do części dziesiętnych: {round_pi}')

print(f'Przybliżenie liczby pi do części dziesiętnych: {pi:.2f}')
#%%
print ('-'*40)
print ('WERSJA: 1.0.1')
print ('-'*40)
#%%

print('='*40)
print ('autor: jannowak@poczta.com')
print ('data: 01-01-2021')
print ('='*40)
#%%
print ('summer', 'time', 'holiday', sep='#')
#%%
pi = 3.1415926535
promien = float(input('Podaj promien: '))
pole = pi* promien**2
print(f'Pole koła wynosi: {pole:.1f} cm2')
#%%
kwota = 1000
stopa = 0.03
lata = 5
zwrot = kwota*(1+stopa)**lata
print(f'Wartość końcowa inwestycji wynosi: {zwrot:.2f} PLN')
#%%
a=3
b=-4
c=1
delta= b**2 - 4* a * c
print ('Delta wynosi:', delta)
#%%
suma = 0
for n in range (10):
    suma += 10 + 4 * (n+1) 
print (f'Suma pierwszych 10 wyrazów ciągu wynosi: {suma:.1f}')

a1 = 14
a10 = 50
n = 10
s10 = ((a1 + a10) / 2) * n
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {s10}')
#%%
suma = 0
for n in range (6):
    suma += 8*2**(n) 
print (f'Suma pierwszych 6 wyrazów ciągu wynosi: {suma:.1f}')

a1 = 8
q = 2
suma = a1 * ((1-q**6)/(1-q))
print (f'Suma pierwszych 6 wyrazów ciągu wynosi: {suma:.1f}')

a1 = 8
a2 = 8 * 2
n = 6
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
print(f'Suma pierwszych {n} wyrazów ciągu wynosi: {s6}')
#%%
a =1
b =5
c =4

suma = -b/a
iloczyn = c*a

print (f'x1+x2 = {suma:.1f}')
print (f'x1x2 = {iloczyn:.1f}')
#%%
wspolrzedneXA = float (input ('podaj wspolrzedna X punktu A'))
wspolrzedneYA = float (input ('podaj wspolrzedna Y punktu A'))
wspolrzedneXB = float (input ('podaj wspolrzedna X punktu B'))
wspolrzedneYB = float (input ('podaj wspolrzedna Y punktu B'))
# A = (2, 4), B = (-4, 6)

wspolrzedneXA = 2
wspolrzedneYA = 4
wspolrzedneXB = -4
wspolrzedneYB = 6
x = (wspolrzedneXB + wspolrzedneXA)/2
y = (wspolrzedneYB + wspolrzedneYA)/2
print (f'Środek odcinka AB: {x},{y}')

#%%
import math
wspolrzedneXA = float (input ('podaj wspolrzedna X punktu A'))
wspolrzedneYA = float (input ('podaj wspolrzedna Y punktu A'))
wspolrzedneXB = float (input ('podaj wspolrzedna X punktu B'))
wspolrzedneYB = float (input ('podaj wspolrzedna Y punktu B'))
# A = (2, 4), B = (-4, 6)

# wspolrzedneXA = 2
# wspolrzedneYA = 4
# wspolrzedneXB = -4
# wspolrzedneYB = 6
d = math.sqrt((wspolrzedneXB-wspolrzedneXA)**2 + (wspolrzedneYB-wspolrzedneYA)**2 ) 
print (f'Długoć odcinka AB: {d}')

a1 = 3
a2 = 2
b1 = -1
b2 = -1
distance = ((b1 - a1) ** 2 + (b2 - a2) ** 2)**(1/2)
print(f'Odległość punktów A i B wynosi: {distance}')
#%%
import math

a= 3
b= 4.5
c= 5
d= 4

srednia = (a*b*c*d)**0.25
print (f'Średnia geometryczna podanych liczb:{srednia:.2f}')
#%%
a1 = 1
a2 = 1/2
q = a2 / a1
S = a1 / (1 - q)
print(f'Suma ciągu wynosi: {S}')
#%%
import math
licznik = 0
gora = 0
suma = 0
while True:
    n = float (input ('podaj kolejna liczbe'))
    if n==0: break
    suma += n
    print(suma)
    licznik += 1
    print (licznik)
    srednia = suma / licznik
    print (srednia)
    gora += (n - srednia)**2
    odchylenie = gora/licznik
    odchylenie = math.sqrt (odchylenie)
    print (f'Odchylenie standardowe: {odchylenie:.2f}')



x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3.0
var = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3.0
std = var**(1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {std:.2f}')

#%%





