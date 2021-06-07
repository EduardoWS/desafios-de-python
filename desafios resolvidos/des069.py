def linha():
    print()
    print('=' * 80)
    print()
linha()

sexo = ''
si = 0
h = 0
mi = 0
while True:
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper()
    
    if idade > 18:
        si += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        mi += 1
    
    perg = str(input('Continuar? [S/N] ')).upper()
    if perg == 'N':
        break
    sexo = ''
    print()
print()
print(f'''
{si} pessoas tem mais de 18 anos
{h} homens cadastrados
{mi} mulheres com menos de 20 anos
''')
linha()
