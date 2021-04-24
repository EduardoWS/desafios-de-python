def linha():
    print()
    print('=' * 80)
    print()
linha()
a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
print()
soma = a1
for n in range(1, 11):
    print(f'A{n} = {soma}')
    soma += r
linha()
