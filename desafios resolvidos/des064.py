def linha():
    print()
    print('=' * 80)
    print()
linha()

num = 0
soma = 0
cont = 0
while not num == 999:
    num = int(input('Valor: '))

    if num != 999:
        soma += num
        cont += 1
print()
print(f'Valores digitados: {cont}')
print(f'Soma dos valores: {soma}')
linha()
