# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:58:58 2022

@author: Marcin
"""
#%%
x = -1.5
expression = 'x**2 + x'

print (eval(expression))
#%%
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

lista = [var1, var2, var3, var4, var5]
for var in lista:
    print(isinstance (var, tuple))
#%%
characters = ['k', 'b', 'c', 'j', 'z', 'w']

print(f'Pierwsza: {min(characters)}')
print(f'Ostatnia: {max(characters)}')
#%%

ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

print(list(zip(ticker, full_name)))
#%%
items = (' ', '0', 0.1, True)
        
print (all(items))
#%%
items = ('', 0.0, 0, False)

print (any(items))
# ciekawa funkcja sprawdzająca czy wszystko lub niektóre jest prawdą w tupli
#%%
number = 3275
print (str(bin(number))[2:].count("1"))
print ((bin (number))[2:])
#%%

def maximum (x: int, y: int, z):
    return max (x,y,z)

print (maximum(-4,2, 5))
#%%

def multi (numbers):
    result = 1
    for number in numbers:
        result *= number    
    return result

print (multi((-4,6,2)))

#%%

def map_longest(lista:list):
    longest_word = ""    
    for word in lista:
        if len(word)>len (longest_word):
            longest_word = word
    return len (longest_word)

def map_longest2(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)
    

print (map_longest(['python', 'sql']))
print (map_longest(['java', 'sql', 'r']))
print (map_longest2(['python', 'sql']))
print (map_longest2(['java', 'sql', 'r']))

#%%
def filter_ge_6(lista:list):
    result =[]
    for word in lista:
        if len(word)>= 6:
            result.append(word)
    return result

print (filter_ge_6(['programowanie', 'python', 'java', 'sql']))
print (filter_ge_6(['java', 'sql']))

#%%
def factorial(n:int):
    result = 1
    i=1
    while i<=n:
        result *= i
        i+=1
    return result
    

print (factorial(6))
print (factorial(10))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
#%%
def count_str(items):
    result =0
    for item in items:
        if isinstance(item, str):
            result +=1
    return result

print (count_str(['p', 2, 4.3, None]))
print (count_str({'p', 2, 4.3, True, 'True', None}))
#%%
def count_str(items):
    result =0
    for item in items:
        if isinstance(item, str):
            if len(item)>2:
                result +=1
    return result

print (count_str([1, '#hello', '', 'python', 'go']))
print (count_str([1, 2, 3, 'python']))

#%%
def remove_duplicates(items:list):
    empty_set = set()
    for item in items:
            empty_set.add(item)
    empty_set= list(empty_set)
    return empty_set

print(remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4]))
print(remove_duplicates([1, 1, 1, 1]))


def remove_duplicates2(items):
    return list(set(items))

#%%
def is_distinct(lista:list):
    if len(set(lista)) < len(lista):
           return True
    else:
           return False
def is_distinct2(items):
    return len(items) == len(set(items))     
        

print (is_distinct([1, 2, 3]))
print (is_distinct([1, 2, 3, 3]))
    
#%%
def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)

function(3)
function(5, ['a', 'b', 'c'])
function(6, [6,3,7,6])
function(4)
#%%

def function(*args, **kwargs):
    print(args, kwargs)

function(3, 4)
function(x=3, y=4)
function(1, 2, x=3, y=4)

#%%

def is_palindrome(item: str):
    reverse = item[::-1]
    return item == reverse

print (is_palindrome('kajak'))
print (is_palindrome('ocena'))











