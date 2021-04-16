def linha():
    print()
    print('=' * 80)
    print()
linha()

nasc = int(input('Ano de nascimento: '))

ano = 2021 - nasc

print()
if ano <= 9:
    print(f'Sua categoria: MIRIM')
elif 9 < ano <= 14:
    print(f'Sua categoria: INFANTIL')
elif 14 < ano <= 19:
    print(f'Sua categoria: JUNIOR')
elif 19 < ano <= 20:
    print(f'Sua categoria: SÊNIOR')
elif ano > 20:
    print(f'Sua categoria: MASTER')
linha()
