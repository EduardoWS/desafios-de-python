def linha():
    print()
    print('=' * 80)
    print()
linha()

lista = []
for n in range(1, 6):
    peso = int(input('Peso (Kg): '))
    lista += [peso]
print()
print(f'Maior peso: {max(lista)}kg')
print(f'Menor peso: {min(lista)}kg')

linha()
