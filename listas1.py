# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:23:43 2021

@author: Pete Hall
"""
lista1=[]
lista2=[]
lista=['R1','R2','R3','S1','S2']
for i in lista:
    if "S" in i:
        lista1.append(i)
    elif 'R' in i:
        lista2.append(i)