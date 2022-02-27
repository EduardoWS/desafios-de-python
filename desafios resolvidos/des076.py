def linha():
    print()
    print('=' * 80)
    print()
linha()

tupla = ('Caneta', '5.99',
         'Borracha', '2.50',
         'Caderno', '15.89',
         'Vassoura', '24.60',
         'Apontador', '7.59')


for n in range(0, int(len(tupla))):
    if n % 2 == 0:
        num = 50-int(len(tupla[n]))
        print(f'{tupla[n]}', '.' * num, f'R${tupla[n+1]}')

linha()
