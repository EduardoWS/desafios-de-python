def linha():
    print()
    print('=' * 80)
    print()
linha()

ano = int(input('Ano de nascimento: '))
idade = 2021 - ano

print()
print(f'Você tem {idade} anos de idade.')

if idade > 18:
    print('Já passou do tempo de se alistar')
    p = 2021 - (ano + 18)
    print(f'Faz {p} anos que você se alistou ou que deveria ter se alistado!')

elif idade == 18:
    print('Você deve se alistar esse ano!')

else:
    print(f'Você ainda é muito novo para se alistar!')
    p = (ano + 18) - 2021
    print(f'Você poderá se alistar daqui {p} anos.')

linha()
