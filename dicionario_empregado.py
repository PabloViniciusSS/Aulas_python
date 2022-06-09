# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:08:57 2022

@author: Pablo VInícius
"""

import datetime  

current_time = datetime.datetime.now() 
ano = current_time.year
    
def idade(n):
   return  ano - n

def aposentadoria(n):
    return  65 - n

pessoa = dict()



pessoa['Nome'] = str(input("Nome: "))
ano_nasc = int(input("Ano de Nascimento: "))
pessoa['Idade'] = idade(ano_nasc)
pessoa['CTPS'] = int(input('Digite numero da cateria de trabalho: '))


if pessoa['CTPS']  != 0:
    pessoa['Ano_contatacao'] = int(input("Ano de contratação: "))
    pessoa['Salario'] = float(input('Salário: '))

pessoa['Aposentadoria'] = aposentadoria(pessoa['Idade'])


print(f'Nome: {pessoa["Nome"]}')
print(f'Idade: {pessoa["Idade"]}')
print(f'CTPS: {pessoa["CTPS"]}')
print(f'Ano de contratação: {pessoa["Ano_contatacao"]}')
print(f'Salario: {pessoa["Salario"]}')
print(f'Aposentadoria: {pessoa["Aposentadoria"]} anos')