def linha():
    print()
    print('=' * 80)
    print()
linha()
soma = 0
val = 0
for n in range(1, 501):
    if n % 3 == 0 and n % 2 != 0:
        soma += n
        val += 1
print(f'A soma de todos os {val} valores solicitados é {soma}')
linha()
