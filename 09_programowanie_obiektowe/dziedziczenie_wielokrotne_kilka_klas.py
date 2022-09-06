# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:30:54 2022

@author: Marcin
"""

class A:
    def metoda(self):
        print('Metoda klasy A')
        
class B(A):
    # def metoda(self):
    #     print('Metoda klasy B')
    pass
        
class C(A):
    # def metoda(self):
    #     print('Metoda klasy C')
    pass
        
class D(B, C):
        # def metoda(self):
        #     print('Metoda klasy D')
        pass

d = D()
d.metoda()
