print('''
[1] = soma  
[2] = subtração
multiplicacao 
divisao = 4''')

opcao = int(input('Qual sua opcao (1/5): '))



num1 = int(input('Valor: '))
num2 = int(input('Valor: '))

if opcao ==  1:
    print(f'{num1} + {num2} = {num1 + num2}')
elif opcao == 2:
    print(f'{num1} - {num2} = {num1 - num2}')
elif opcao == 3:
    print(f'{num1} X {num2} = {num1 * num2}')
elif opcao == 4:
    print(f'{num1}  / {num2} = {num1 / num2}')


