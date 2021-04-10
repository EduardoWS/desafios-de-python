import os
from time import sleep


def linha():
    print()
    print('=' * 80)
    print()
linha()

while True:
    def num():
        try:
            global n
            n = int(input('Digite um número: '))
            n + 1
        except:
            print('Digite um número inteiro abestado. ')
            num()
    
    num()

    print()
    print('Escolha uma base de conversão:')
    print()
    print(' [1] binário \n [2] octal \n [3] hexadecimal \n [0] sair')
    print()
    escolha = int(input('Sua escolha: '))
    print()

    if escolha == 1:
        bi = bin(n)
        print(f'{n} em binário é: {bi[2:]}')
        sleep(5)
        os.system('cls') or None
        linha()

    elif escolha == 2:
        oc = oct(n)
        print(f'{n} em octal é: {oc[2:]}')
        sleep(5)
        os.system('cls') or None
        linha()

    elif escolha == 3:
        he = hex(n)
        print(f'{n} em hexadecimal é: {he[2:]}')
        sleep(5)
        os.system('cls') or None
        linha()

    elif escolha == 0:
        break

    print()
linha()
