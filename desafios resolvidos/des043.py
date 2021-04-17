def linha():
    print()
    print('=' * 80)
    print()
linha()
peso = float(input('Peso (KG): '))
altura = float(input('Altura (metros): '))

imc = peso / (altura**2)

print()
if imc < 18.5:
    print(f'Seu IMC: {imc:.2f}')
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC: {imc:.2f}')
    print('Peso ideal!')
elif 25 <= imc < 30:
    print(f'Seu IMC: {imc:.2f}')
    print('Sobrepeso!')
elif 30 <= imc <= 40:
    print(f'Seu IMC: {imc:.2f}')
    print('Obesidade!!')
elif imc > 40:
    print(f'Seu IMC: {imc:.2f}')
    print('Obesidade mórbida!!!')
linha()
