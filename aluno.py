# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:18:23 2022

@author: Pablo Vinícius
"""
aluno = dict()


aluno['Nome'] = str(input('Digite o Nome: '))
aluno['Media'] = float(input('Digte a média: '))
    
if aluno['Media'] < 5:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Aprovado'

   
print(f'O nome é {aluno["Nome"]} ')
print(f'Tem média igual á {aluno["Media"]}')
print(f'{aluno["Situacao"]}')
            