print()
print('=' * 80)
d = int(input('Distância da viagem(Km): '))

if d <= 200:
    p = 0.5 * d
    print(f'Preço da viagem: R${p:.2f}')

else:
    p = 0.45 * d
    print(f'Preço da viagem: R${p:.2f}')

print()
print('=' * 80)
print()
