import os
def linha():
    print()
    print('=' * 80)
    print()

perg = '1'
while not perg == '0':
    linha()
    a1 = int(input('Digite o primeiro termo de uma PA: '))
    r = int(input('Digite a razão da PA: '))
    print()
    termos = int(input('Quantos termos da PA quer mostrar: '))
    print()
    soma = a1
    cont = 1
    

    while not cont == termos+1:
        print(f'A{cont} = {soma}')
        soma += r
        cont += 1
    print()
    perg = str(input('''Novos valores? Digite qualquer tecla para continuar e 0 para sair.
>> '''))
    if perg != '0':
        os.system('cls')
    
linha()
