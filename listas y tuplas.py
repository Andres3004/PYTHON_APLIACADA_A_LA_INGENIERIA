# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:22:57 2021

@author: Andres Herrera
"""

lista1=[2,True,5.8,"CEC",2,False]
tupla=(2,True,5.8,"CEC",2,False)
print(type(lista1))
print(type(tupla))
print(lista1)
print(tupla)
print(lista1[0])
print(lista1[-6])
print(tupla[0])
print(tupla[-6])
lista1[4]=6
del lista1[5]
tupla[4]=6
del tupla[4]