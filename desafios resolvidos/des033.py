def linha():
    print()
    print('=' * 80)
    print()
linha()

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

lista = [n1, n2, n3]
lista.sort()                          #esse comando organiza do menor pro maior
maior = lista[2]
menor = lista[0]

print()
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
linha()
