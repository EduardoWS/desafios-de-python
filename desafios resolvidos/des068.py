import random
import os
from time import sleep
def linha():
    print()
    print('=' * 80)
    print()

cont = 0
while True:
    linha()
    valor = int(input('Digite um valor: '))
    pi = str(input('Par ou ímpar? [P/I] ')).upper()
    pc = random.randint(0, 10)
    soma = pc + valor
    if soma % 2 == 0 and pi == 'P':
        print()
        print(f'Você jogou {valor} e o PC jogou {pc}. A soma deu {soma} que é PAR')
        print('VOCÊ GANHOU!')
        cont += 1
        sleep(10)
        os.system('cls')
    elif soma % 2 == 0 and pi == 'I':
        print()
        print(f'Você jogou {valor} e o PC jogou {pc}. A soma deu {soma} que é PAR')
        print('VOCÊ PERDEU!')
        print('-' * 80)
        print(f'Você ganhou {cont} vezes seguidas!')
        break
    elif soma % 2 != 0 and pi == 'I':
        print()
        print(f'Você jogou {valor} e o PC jogou {pc}. A soma deu {soma} que é ÍMPAR')
        print('VOCÊ GANHOU!')
        cont += 1
        sleep(10)
        os.system('cls')
    elif soma % 2 != 0 and pi == 'P':
        print()
        print(f'Você jogou {valor} e o PC jogou {pc}. A soma deu {soma} que é ÍMPAR')
        print('VOCÊ PERDEU!')
        print('-' * 80)
        print(f'Você ganhou {cont} vezes seguidas!')
        break
linha()
