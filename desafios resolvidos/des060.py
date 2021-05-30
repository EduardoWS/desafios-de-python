def linha():
    print()
    print('=' * 80)
    print()
linha()

num = int(input('valor: '))

fat = num
print(f'{num}! = {num}', end='')
for n in range(num-1, 0, -1):
    fat = fat * n
    print(f' x {n}', end='')
    
print(f' = {fat}')
linha()
