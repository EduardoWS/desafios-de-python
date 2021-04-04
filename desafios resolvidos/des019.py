import random
from time import sleep
print()
print('=' * 40)
n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')

lista = [n1, n2, n3, n4]
sort = random.choice(lista)

print('Sorteando...')
sleep(1.5)
print()
print(f'O aluno sorteado foi: {sort}')
print()
print('=' * 40)
print()
