def linha():
    print()
    print('=' * 80)
    print()
linha()
perg = ''
lista = []
soma = 0
while not perg == 'N':
    num = int(input('Valor: '))
    lista += [num]
    soma += num
    perg = str(input('''Continuar? [S/N]
>> ''')).upper()

media = soma / len(lista)
print()
print(f'A média desses valores é {media}')
print(f'O maior valor é {max(lista)}')
print(f'O menor valor é {min(lista)}')
linha()
