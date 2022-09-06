# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:47:22 2022

@author: Marcin
"""
import time
import sys


class Magazyn:
    
    
    def __init__ (self, lista_produktow):
        self.lista_produktow = lista_produktow
        
    def wyswietl_dostepne_produkty(self):
        print('Dostępne produkty: ')
        for product in self.lista_produktow:
            print(product)
            
    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu: \n>>>  ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
            print(f'Produkt{self.nazwa_produktu} został dodany do magazynu')
        else:
            print (f'Produkt{self.nazwa_produktu} już jest na liscie')
    
    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu do usunięcia: \n>>>  ')
        if self.nazwa_produktu in self.lista_produktow:
          self.lista_produktow.remove (self.nazwa_produktu)
          print('Usunieto produkt z magazynu')
        else:
            print('Nie ma takiego produktu na liscie produktow')

magazyn = Magazyn(['mleko', 'woda', 'jajka'])


while True:
    
    print ('Wprowadz 1 aby wyswietlic stan magazynu')
    print ('Wprowadz 2 aby dodac produkt') 
    print ('Wprowadz 3 aby usunac produkt')         
    print ('Wprowadz 4 aby zakonczyc') 
    
    wybor_uzytkownika = int( input('>>>'))
    
    
    if wybor_uzytkownika == 1:
            magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownika == 2:
            magazyn.dodaj_produkt()
    elif wybor_uzytkownika == 3:
            magazyn.usun_produkt()
    else:
            print('Koniec programu')
            sys.exit()
    time.sleep(1)
    print ('...')
    time.sleep(1)
    print ('...')
    time.sleep(1)
    print ('...')
            
            
    
            
    