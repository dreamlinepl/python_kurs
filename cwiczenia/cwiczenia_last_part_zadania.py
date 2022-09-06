# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:43:23 2022

@author: Marcin
"""

y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]


def accuracy(y_true, y_pred):
    counter = 0
    for i, j in zip(y_true, y_pred):
        if i == j:
            counter += 1
    return round(counter / len(y_true), 4)


correct = 0
for idx in range (0, len(y_true)):
    if y_pred[idx] == y_true[idx]:
        correct += 1
        


# print (f'Accuracy: {accuracy:.4f}')

print (accuracy(y_true, y_pred))
#%%

y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]


def mae(y_true,y_pred):
    suma = 0
    for i, j in zip (y_true, y_pred):
        suma += abs(j-i)
    return round( suma/len (y_true),3)


print (mae(y_true, y_pred))

#%%


def mae(y_true, y_pred):
    return round(sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)]) / len(y_true), 3)

y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]

print (mae(y_true, y_pred))
#%%

def mse(y_true, y_pred):
    return round(sum([(i[1] - i[0])**2 for i in zip(y_true, y_pred)]) / len(y_true), 3)

y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
mse(y_true, y_pred) 
#%%
def relu(x):
    return max(x,0)

print (relu (4))
#%%
def flatten(lista):
    flatten = list()
    for i in range(len(lista)):
        for j in range (len (lista[i])):
            flatten.append(lista[i][j])
    return flatten

def flatten1(items):
    result = []
    for item in items:
        result.extend(item)
    return result

items = [ [1, 2, 3],[4, 5, 6],[7, 8, 9]]

print (items)
print (flatten(items))
print (flatten1(items))
#%%
def transfer_zeros(items):
    result = []
    counter =0
    for item in items:
        if item != 0:
            result.append(item)
        else:
            counter += 1
    for i in range (counter):
        result.append ("0")
    return result    



print (transfer_zeros([3, 4, 0, 2, 0, 5, 1, 6, 2]))
#%%
from math import sqrt

def euclidean_distance(a,b):
    result = sqrt ((a[0] - b[0])**2+(a[1]-b[1])**2)
    return result

def euclidean_distance1(x, y):
    squared_diff = [(i - j)**2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5

print (euclidean_distance([0, 3], [4, 0]))
    
#%%
def arrange(start, stop, step=1):
    result = []
    i = start;
    while i < stop:
        result.append (i)
        i+=step
        
    return result

def arrange1(start, stop, step=1):
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result


print (arrange1(0, 10))
print (arrange1(0, 10, 2))
#%%
def concat(x,y):
    result = []
    para =[ x[0][0],y[0][0]]
    result.append (para)
    para =[ x[1][0],y[1][0]]
    result.append (para)
    return result

def concat1(l1, l2):
    result = []
    for i, j in zip(l1, l2):
        result.append([i[0], j[0]])
    return result

l1 = [[1], [2]]
l2 = [[3], [4]]

print (concat1(l1,l2))

#%%
def identity(n):
    result = []
    for i in range (n):
        row = []
        for j in range (n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result

def identity1(n):
    array = [[0]*n for i in range(n)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array

print (identity1 (2))
print (identity1 (3))
print (identity1 (4))

#%%

def fill_value(height, width, value):
    result = []
    for i in range (height):
        row = []
        for j in range (width):
            row.append(value)
        result.append(row)          
    return result

def fill_value1(height, width, value):
    return [[value] * width for i in range(height)]

        
        
fill_value1(height=2, width=3, value=255)     
fill_value1(4, 2, 'a')
#%%
def trace (array):
    suma = 0
    for i in range (len (array[0])):
        suma += array[i][i]
    return suma



trace([[1, 2], [4, 2]])
trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]])
   
#%%
def transpose(array):
    width = len (array[0])
    height = len (array)
    new_array = [[0] * height for i in range(width)]
    for i in range (height):
        for j in range (width):
            new_array [j][i] = array [i][j]
    print (new_array)

def transpose1(array):
    width = len(array[0])
    result = []
    
    for i in range(width):
        pair = []
        for item in array:
            pair.append(item[i])
        result.append(pair)
    return result

transpose([[1, 2, 3], [4, 5, 6]])
transpose([[1, 2], [3, 4], [5, 6]])
transpose([[1, 2, 3, 4], [5, 6, 7, 8]])
#%%

def max_prob(array):
    max_prob = []
    for row in array:
        max_prob_row = 0
        for item in row:
            if item >  max_prob_row:
                max_prob_row = item
        max_prob.append(max_prob_row)
    
    return max_prob

def max_prob1(array):
    result = []

    for item in array:
        max_val = max(item)
        for idx, val in enumerate(item):
            if val == max_val:
                result.append([val])
    return result

print (max_prob1([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9]]))
print( max_prob1([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]])   )
print (max_prob1([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.4, 0.3, 0.3]]) )
#%%
def detect_class(array):
    result = []
    for item in array:
        max_val = max(item)
        row = []
        for idx, val in enumerate(item):
            if val == max_val:
                row.extend([1])
            else:
                row.extend([0])
        result.append(row)
    return result

def detect_class1(array):
    result = []

    for item in array:
        max_val = max(item)
        empty = [0] * len(item)
        for idx, val in enumerate(item):
            if val == max_val:
                empty[idx] = 1
                result.append(empty)
    return result

print(detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]]) )
print (detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.3, 0.3, 0.4]]))

#%%
def dot_product(v,w):
    suma =0
    for i in range (len (v)):
        suma += v[i] * w[i]  
    return suma
def dot_product1(vec1, vec2):
    return sum([v * w for v, w in zip(vec1, vec2)])

print (dot_product([1, 2], [5, 2]))
#%%
def count_none(lista):
    result = 0
    for i in lista:
        if i == None:
            result +=1

    return result

def count_none1(items):
    counter = 0
    for item in items:
        if not item:
            counter += 1
    return counter
    
print (count_none1([1, None, None, 5, None, 2]))


#%%
def top_n (lista, n):
    result = []
    for i  in range (n):
        max_act = max(lista)
        result.append(max_act)
        lista.remove(max_act)
    return result

def top_n1(items, n):
    items.sort(reverse=True)
    return items[:n]
        
print (top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3))


































































        
    



















