#jokenpo
import random
import os
from time import sleep

def linha():
    print()
    print('=' * 80)
    print()
linha()

while True:
    lista = ['Pedra', 'Papel', 'Tesoura']
    pc = random.choice(lista)
    print('''Faça sua escolha:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
    e = input('>> ')
    print()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print()
    if e == '1' and pc == 'Pedra' or e == '2' and pc == 'Papel' or e == '3' and pc == 'Tesoura':
        print(f'Escolha do pc: {pc}')
        print('EMPATE!')
        print()
        print('Digite 1 para jogar de novo e qualquer tecla para sair')
        escolha = input('>> ')
        if escolha == '1':
            print('Carregando...')
            sleep(2)
            os.system('cls') or None
            print()
        else:
            print('Saindo...')
            sleep(1.5)
            break
    elif e == '1' and pc == 'Papel' or e == '2' and pc == 'Pedra':
        print(f'Escolha do pc: {pc}')
        if e == '1':
            print('VOCÊ PERDEU!')
        elif e == '2':
            print('VOCÊ GANHOU!')
        print()
        print('Digite 1 para jogar de novo e qualquer tecla para sair')
        escolha = input('>> ')
        if escolha == '1':
            print('Carregando...')
            sleep(2)
            os.system('cls') or None
            print()
        else:
            print('Saindo...')
            sleep(1.5)
            break
    
    elif e == '1' and pc == 'Tesoura' or e == '3' and pc == 'Pedra':
        print(f'Escolha do pc: {pc}')
        if e == '3':
            print('VOCÊ PERDEU!')
        elif e == '1':
            print('VOCÊ GANHOU!')
        print()
        print('Digite 1 para jogar de novo e qualquer tecla para sair')
        escolha = input('>> ')
        if escolha == '1':
            print('Carregando...')
            sleep(2)
            os.system('cls') or None
            print()
        else:
            print('Saindo...')
            sleep(1.5)
            break
    elif e == '2' and pc == 'Tesoura' or e == '3' and pc == 'Papel':
        print(f'Escolha do pc: {pc}')
        if e == '2':
            print('VOCÊ PERDEU!')
        elif e == '3':
            print('VOCÊ GANHOU!')
        print()
        print('Digite 1 para jogar de novo e qualquer tecla para sair')
        escolha = input('>> ')
        if escolha == '1':
            print('Carregando...')
            sleep(2)
            os.system('cls') or None
            print()
        else:
            print('Saindo...')
            sleep(1.5)
            break
    else:
        print('ERROR')
linha()
