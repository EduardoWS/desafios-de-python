import os
def linha():
    print()
    print('=' * 80)
    print()


while True:
    linha()
    print('{:^80}'.format('BANCO DA CORÉIA'))
    valor = int(input('SACAR: R$'))
    print()
    ced = 100
    total = valor
    totced = 0

    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                if totced == 1:
                    print(f'Total de {totced} cédula de R${ced},00')
                else:
                    print(f'Total de {totced} cédulas de R${ced},00')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            totced = 0
            if total == 0:
                break
    print()
    perg = str(input('NOVOS VALORES? [S/N] ')).upper()
    if perg == 'N':
        break
    print()
    os.system('cls')
linha()
