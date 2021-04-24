print()
print('=' * 80)
num = int(input('Digite um número para ver sua tabuada: '))
print()

for c in range(1, 11):
    print(f'{num} x {c:>2} = {num*c:>2}')

print()
print('=' * 80)
print()