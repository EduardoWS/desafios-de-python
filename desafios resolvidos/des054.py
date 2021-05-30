from datetime import date
def linha():
    print()
    print('=' * 80)
    print()
linha()

contmaior = 0
contmenor = 0
for n in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    atual = date.today().year
    if atual - ano >= 18:
        contmaior += 1
    elif atual - ano < 18:
        contmenor += 1
    else:
        print(f'Error: {n}')
        
print()
print(f'{contmaior} pessoas são maiores de idade.')
print(f'{contmenor} pessoas são menores de idade.')

linha()
