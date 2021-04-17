def linha():
    print()
    print('=' * 80)
    print()
linha()
p = float(input('Preço: R$'))
print()
print('''Escolha a forma de pagamento:

[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print()
e = input('>> ')
print()
if e == '1':
    d = p * 90/100
    print(f'Valor do produto: R${p:.2f}')
    print(f'Desconto: 10%')
    print(f'Total: R${d:.2f}')
elif e == '2':
    d = p * 95/100
    print(f'Valor do produto: R${p:.2f}')
    print(f'Desconto: 5%')
    print(f'Total: R${d:.2f}')
elif e == '3':
    print(f'Valor do produto: R${p:.2f}')
    print(f'Desconto: 0%')
    print(f'Total: R${p:.2f}')
elif e == '4':
    d = p * 120/100
    print(f'Valor do produto: R${p:.2f}')
    print(f'Juros: 20%')
    print(f'Total: R${d:.2f}')
else:
    print('ERROR')
linha()
