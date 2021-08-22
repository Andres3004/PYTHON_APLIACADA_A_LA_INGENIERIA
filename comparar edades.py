# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:47:22 2021

@author: Andres Herrera
"""
print("")
print("Bienvenido por favor ingrese los siguientes datos:")
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
space=" "
print(" ")
print("Sus datos completos son:" '\n')
print("Nombre:    " +space+nombre+"\n")
if edad>=1 and edad <=12:
    print('Usted es un nino')
elif edad>=13 and edad <=18:
    print('Usted es un joven')
else:
    print('Usted es un adulto')

