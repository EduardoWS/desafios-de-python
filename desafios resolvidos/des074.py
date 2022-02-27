from random import randint

def linha():
    print()
    print('=' * 80)
    print()
linha()

tupla = ()
for n in range(0, 5):
    num = randint(0, 100)
    tupla += (num,)
    
print('numeros gerados:')
print()

for n in range(0, 5):
    print(f'{tupla[n]}')

print()
print(f'Menor número gerado: {sorted(tupla)[0]}')
print(f'Maior número gerado: {sorted(tupla)[-1]}')

linha()
