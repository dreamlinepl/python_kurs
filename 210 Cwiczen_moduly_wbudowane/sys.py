# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:45:13 2022

@author: Marcin
"""
import sys
print(sys.executable)
print (sys.path)

for arg in sys.argv[1:]:
    print(arg)