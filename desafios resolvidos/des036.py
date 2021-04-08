def linha():
    print()
    print('=' * 80)
    print()
linha()

casa = float(input('Valor da casa: R$'))
s = float(input('Seu salário: R$'))
anos = int(input('Anos: '))
print()

conv = anos * 12
pm = casa / conv
danger = s * 30/100

if  pm < danger:
    print(f'Prestação Mensal: R${pm:.2f}')
    por = (pm * 100) / s
    print(f'A prestação Mensal é {por:.2f}% do seu salário!')
    print('Empréstimo Aceito!!')

else:
    print(f'Prestação Mensal: R${pm:.2f}')
    por = (pm * 100) / s
    print(f'A prestação Mensal é {por:.2f}% do seu salário!')
    print('Empréstimo Negado!!')
linha()
