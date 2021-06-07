def linha():
    print()
    print('=' * 80)
    print()
linha()

total = cont = 0
lista = []
val = 0
while True:
    nome = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    val += 1
    if val == 1 or valor < b:
        nomeb = nome
        b = valor

    if valor > 1000:
        cont += 1
    total += valor

    perg = ' '
    while perg not in 'SN':
        perg = input('Continuar? [S/N] ').upper().strip()[0]
    if perg == 'N':
        break
    print()

print()
print(f'''
Total gasto: R${total:.2f}
{cont} produtos custam mais de R$1000
{nomeb} é o produto mais barato
''')
linha()
