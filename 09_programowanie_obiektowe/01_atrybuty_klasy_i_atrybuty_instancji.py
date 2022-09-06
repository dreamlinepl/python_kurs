# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

class Drzewo:

    nazwa = str
    wiek = int
    wysokosc = int


drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %%
print(id(drzewo_1))
print(id(drzewo_2))

# %%
dir(drzewo_1)

# %%

drzewo_1.nazwa = 'Sosna'
drzewo_1.wiek = 12
drzewo_1.wysokosc = 40
print (drzewo_1.nazwa)
print (drzewo_1.wiek)
print (drzewo_1.wysokosc)

# %%
print (drzewo_2.nazwa)
print (drzewo_2.wiek)
print (drzewo_2.wysokosc)


# %%
drzewo_1.stan = 'dobry'

print(dir(drzewo_2))

# %%
Drzewo.miejsce = 'las'

# %%
print(dir(drzewo_2))
print(drzewo_2.miejsce)

drzewo_2.miejsce = 'park'

print(drzewo_2.miejsce)
print(drzewo_1.nazwa)














