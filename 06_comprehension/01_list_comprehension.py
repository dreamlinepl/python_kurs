# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

results = []
for i in range(100):
    results.append(i**2)
    print(results)

results = []
for i in range(100):
    results.append(i**2)
    print(results)

results = []
for i in range(100):
    results.append(i**2)
    print(results)


results = []
for i in range(100):
    results.append(i**2)
    print(results)


results = []
for i in range(100):
    results.append(i**2)
    print(results)


results = []
for i in range(100):
    results.append(i**2)
    print(results)


results = []
for i in range(100):
    results.append(i**2)
    print(results)


results = []
for i in range(100):
    results.append(i**2)
    print(results)

results = []
for i in range(100):
    results.append(i**2)
    print(results)

results = []
for i in range(100):
    results.append(i**2)
    print(results)



# %%
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)
results_2 = [i**2 for i in range(100)]
print(results_2)

# %%
lista = [i * 3 for i in range(100)]

# %%
results = []
for i in range(100):
    if i % 5 == 0:
        results.append(i**2)

# %%
results_2 = [i ** 2 for i in range(100) if i % 5 == 0]

# %%
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

results = []
for letter in letters:
    for number in numbers:
        results.append(letter + number)

# %%
results_2 = [letter + number for letter in letters for number in numbers]

# %%
ls_1 = ['a', 'b', 'c']
ls_2 = ['a', 'b', 'c']

results = [l_1 + l_2 for l_1 in ls_1 for l_2 in ls_2 if l_1 != l_2]

# %%
[[j for j in range(10)] for i in range(5)]

# %%
[[(i, j) for j in range(10)] for i in range(3)]
# %%
[[i * j for j in range(10)] for i in range(10)]

# %%
[[l1 + l2 for l2 in 'abcde'] for l1 in '12345']

# %%
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


kombinacje = (silnia(49)/(silnia(6) * silnia(43)))
print (kombinacje)


def symbol_newtona(n, k):
    return silnia (n)/(silnia (k) *silnia (n-k))

kombinacje = symbol_newtona (49,6)
trafne = symbol_newtona(12, 6)
print (2772*kombinacje/trafne)
print(3*kombinacje)
#%%

zadanie = [i for i in range (30) if i%4==0]
print (zadanie)













