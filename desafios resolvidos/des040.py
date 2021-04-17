#des040
def linha():
    print()
    print('=' * 80)
    print()
linha()
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1 + n2) / 2

print()
if m < 5:
    print(f'Sua média: {m:.1f}')
    print('REPROVADO!')

elif 5 <= m < 7:
    print(f'Sua média: {m:.1f}')
    print('RECUPERAÇÃO!')

elif m >= 7:
    print(f'Sua média: {m:.1f}')
    print('APROVADO!')

linha()
