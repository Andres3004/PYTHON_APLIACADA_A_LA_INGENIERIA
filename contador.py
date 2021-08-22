# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:26:58 2021

@author: Pete Hall
"""

contar=input('Ingrese el # veces a contar: ')
contar=int(contar)
contador=1
while True:
    print(contador)
    contador=contador+1
    if contador>contar:
        break