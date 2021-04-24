def linha():
    print()
    print('=' * 80)
    print()
linha()
print('Digite 6 números inteiros:')
soma = 0
for n in range(1, 7):
    num = int(input('>> '))
    if num % 2 == 0:
        soma += num
print()
print(f'O resultado da soma dos valores pares digitados é {soma}.')
linha()
