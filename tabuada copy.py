while True:
    n = int(input('Qual a tabuada que você quer saber? '))

    if n < 0:
        break

    for c in range(1, 11):
            print(f'{n} X {c} = {n*c}')

    cont = input('Deseja ver outro valor(s/n): ')

    if cont == 'n':
        break

    

            


