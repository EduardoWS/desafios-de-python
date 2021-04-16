def linha():
    print()
    print('=' * 80)
    print()
linha()
l1 = int(input('Comprimento 1: '))
l2 = int(input('Comprimento 2: '))
l3 = int(input('Comprimento 3: '))
print()
if abs(l1 - l2) < l3 < l1 + l2 and abs(l1 - l3) < l2 < l1 + l3 and abs(l3 - l2) < l1 < l3 + l2:
    print('Com essas medidas da pra formar um triângulo!')
    if l1 == l2 == l3:
        print('É um triângulo EQUILÁTERO.')
    elif l1 != l2 != l3:
        print('É um triângulo ESCALENO.')
    else: 
        print('É um triângulo ISÓSCELES.')
else:
    print('Com essas medida NÃO da para formar um triângulo!')
linha()
