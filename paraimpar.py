from random import randint

v = 0

while True:
    jogador = int(input('Digite um valor '))
    cpu = randint(1,10)
    total = cpu + jogador

    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e a maquina jogou {cpu}. Total {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou')
            v+=1
        else:
            print('Você perdeu')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou')
            v+=1
        else:
            print('Você perdeu')
        
    cont = str(input('Quer jogar novamente?[S/N] ')).strip().upper()[0]
    if cont == 'N':
         break

print(f'Você ganhou {v} ')



    
