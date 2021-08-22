# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:13:24 2021

@author: Andres Herrera
"""
acl=int(input('Ingrese el # de ACL: '))
if acl>=1 and acl <=99:
    print('Es una ACL standard')
elif acl>=100 and acl <=199:
    print('Es una ACL extendida')
else:
    print('El # ingresado no es de una ACL')