def linha():
    print()
    print('=' * 80)
    print()
linha()
sexo = str(input('Sexo [M/F]: ')).upper()

if sexo != 'M' and sexo != 'F':
    cont = 0
    while True:
        if cont == 0:
            print('Por favor, digite corretamente com M para sexo masculino e F para sexo feminino.')
            sexo = str(input('Sexo [M/F]: ')).upper()
            if sexo == 'M' or sexo == 'F':
                print()
                break
            else:
                cont += 1
        elif cont == 1:
            print('Irmão, digite certo igual te ensinei da última vez.')
            sexo = str(input('Sexo [M/F]: ')).upper()
            if sexo == 'M' or sexo == 'F':
                print()
                break
            else:
                cont += 1

        elif cont == 2:
            print('Cara? Qual a dificuldade de digitar M ou F??? Bora acabar com isso logo...')
            sexo = str(input('Sexo [M/F]: ')).upper()
            if sexo == 'M' or sexo == 'F':
                print()
                break
            else:
                cont += 1

        elif cont == 3:
            print('É sério isso? Porra maluco, dá o fora daqui então. Desisto de você!!')
            break
            

if sexo == 'M':
    print(f'Seu sexo é MASCULINO')
elif sexo == 'F':
    print(f'Seu sexo é FEMININO')
linha()
