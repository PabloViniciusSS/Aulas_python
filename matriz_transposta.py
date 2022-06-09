# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 08:54:12 2022

@author: Pablo Vinícius
"""
def imprimeMatriz(C):
    linhas = len(C)
    colunas = len(C[0])
    for i in range(linhas):
        for j in range(colunas):
            print(f'{C[i][j]}')


def transposta(M):
    return list(map(lambda *i: [j for j in i], *M))



matriz = [[1,2],[3,4],[5,6],[7,8]]
for j in matriz:
    print(j)

print("")

dados = transposta(matriz)
for i in dados:
   print(i)
    

