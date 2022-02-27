def linha():
    print()
    print('=' * 80)
    print()
linha()

lista = []
for n in range(0, 5):
    num = int(input(f'{n+1}º valor: '))
    lista += [num]

print()
print(f'O maior valor digitado é {sorted(lista)[-1]} e o menor valor digitado é {sorted(lista)[0]}')
print(f'O maior valor digitado está na posição {lista.index(sorted(lista)[-1])+1}')
print(f'O menor valor digitado está na posição {lista.index(sorted(lista)[0])+1}')

linha()
