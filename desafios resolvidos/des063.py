def linha():
    print()
    print('=' * 80)
    print()
linha()
num = int(input('''Digite um número N para ver N sequências de Fibonacci.
>> '''))
print()
result = 1
um = 1
dois = 0

cont = 0
while True:
    result = um + dois
    print(f'{result}', end=' > ')
    
    um = dois
    dois = result
    result = um + dois
    cont += 1
    
    if cont == num:
        break
print('FIM')
linha()
