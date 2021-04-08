def linha():
    print()
    print('=' * 80)
    print()
linha()

s = float(input('Salário: R$'))

if s > 1250:
    a = s * 110/100
    print(f'Salário atual: R${a:.2f}')

else:
    a = s * 115/100
    print(f'Salário atual: R${a:.2f}')
linha()
