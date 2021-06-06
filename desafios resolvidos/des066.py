def linha():
    print()
    print('=' * 80)
    print()
linha()
soma = cont = 0
while True:
    num = int(input('Digite um valor [999 pra parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print()
print(f'A soma dos {cont} valores é igual a {soma}')
linha()
