def linha():
    print()
    print('=' * 80)
    print()
linha()
tupla = ()
pares = []
for n in range(0, 4):
    num = int(input(f'{n+1}º valor: '))
    tupla += (num,)
    if num % 2 == 0:
        pares += [num]

print()
print(f'O valor 9 apareceu {tupla.count(9)} vez(es).')
if 3 in tupla:
    print(f'O valor 3 apareceu {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

if pares != []:
    p = str(pares)
    p = p.replace('[', '')
    p = p.replace(']', '')
    print(f'Os números pares são: {p}')
else:
    print('Não foi digitado nenhum valor par.')


linha()