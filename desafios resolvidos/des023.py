print()
print('=' * 40)
num = str(input('Digite um número de 0 a 9999: '))

print()

if len(num) == 1:
    print(f'Unidade: {num}')
    print(f'Dezena: 0')
    print(f'Centena: 0')
    print(f'Milhar: 0')

elif len(num) == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
    print(f'Centena: 0')
    print(f'Milhar: 0')

elif len(num) == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')
    print(f'Milhar: 0')

elif len(num) == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')

print()
print('=' * 40)
print()
