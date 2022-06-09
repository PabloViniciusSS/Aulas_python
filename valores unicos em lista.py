# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:30:15 2022

@author: Pablo Vinícius
"""

listanum = list()

while True:
    num = int(input('Digite um número:'))
    if num not in listanum:
        listanum.append(num)
    else:
        print('Número ja adicionado')
       
        
    r = str(input('Quer continuar? [N/S]? '))
    if r in 'Nn':
        break
    
    print(f'Valor adicionado foi {listanum}')   
    
