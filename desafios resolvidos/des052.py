def linha():
    print()
    print('=' * 80)
    print()
linha()
num = int(input('Digite um número inteiro: '))
soma = 0
for n in range(1, num + 1):
    if num % n == 0:
        soma += 1

if soma > 2:
    print(f'O número {num} não é primo.')
else:
    print(f'O número {num} é primo.')
linha()
