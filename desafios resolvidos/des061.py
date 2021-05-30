def linha():
    print()
    print('=' * 80)
    print()
linha()
a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
print()
soma = a1
cont = 1
while not cont == 11:
    print(f'A{cont} = {soma}')
    soma += r
    cont += 1
linha()
