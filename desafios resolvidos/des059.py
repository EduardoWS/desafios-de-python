import os
def linha():
    print()
    print('=' * 80)
    print()
linha()
bandeira = False
perg = 0
while True:
    
    num1 = int(input('1º valor: '))
    num2 = int(input('2º valor: '))
    while not perg == 5:
        print()
        print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    ''')
        print()
        perg = int(input('>> '))
        if perg == 5:
            bandeira = True
            os.system('cls')
            break
        elif perg == 1:
            soma = num1 + num2
            os.system('cls')
            print(f'{num1} + {num2} = {soma}')
        elif perg == 2:
            mult = num1 * num2
            os.system('cls')
            print(f'{num1} x {num2} = {mult}')
            
        elif perg == 3:
            os.system('cls')
            if num1 > num2:
                print(f'O maior número é {num1}')
            elif num2 > num1:
                print(f'O maior número é {num2}')
            else:
                print(f'Os números são iguais.')
            
        elif perg == 4:
            os.system('cls')
            break
        else:
            print('Digite um número que esteja no menu.')
    if bandeira:
        break
linha()