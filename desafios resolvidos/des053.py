def linha():
    print()
    print('=' * 80)
    print()
linha()
frase = str(input('Digite algo: ')).replace(' ', '')
inv = frase[::-1]

if frase == inv:
    print(f'A frase {frase} é um palíndromo!')
else:
    print(f'A frase {frase} não é um palíndromo!!')
linha()
