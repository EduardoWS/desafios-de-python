def linha():
    print()
    print('=' * 80)
    print()
linha()

while True:
    num = int(input('Digite um número para ver sua tabuada [0 para sair]: '))
    print()
    if num == 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:>2} = {num*c:>2}')
    print()
linha()
