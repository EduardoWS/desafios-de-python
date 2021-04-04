from random import shuffle
from time import sleep
print()
print('=' * 40)
n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
print('Sorteando...')
sleep(2)

print()
print(f'Primeiro aluno: {lista[0]}')
print(f'Segundo aluno: {lista[1]}')
print(f'Terceiro aluno: {lista[2]}')
print(f'Quarto aluno: {lista[3]}')
print()
print('=' * 40)
print()
