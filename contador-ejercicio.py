# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:35:37 2021

@author: Andres Herrera
"""

while True:
    x=input("ingrese un numero a contar: ")
    if x=="q" or x=="salir":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break