# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:48:46 2022

@author: Marcin
"""

import string


docs = 'programming in python'
code_map = dict((enumerate(string.ascii_lowercase)))
code_map_inv = {val: key for key, val in code_map.items()}

result = ''
for char in docs:
    if char == ' ':
        result += ' '
        continue
    idx = (code_map_inv[char] + 3) % 25
    result += code_map[idx]

print(result)
#%%

from string import Template
 
 
names = ['John', 'Paul', 'Lisa', 'Michael']
 
email = """Hello $name,
 
Thank you for visiting our website.
Team, XYZ"""
 
template = Template(email)
 
for name in names:
    print(template.substitute(name=name))
    print('-' * 35)