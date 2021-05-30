def linha():
    print()
    print('=' * 80)
    print()
linha()

nomeh = 'None'
muie = 0
homivelho = 0
cont = 0
for n in range(1, 5):
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    if sexo == 'M' and homivelho < idade:
        nomeh = nome
        homivelho = idade
    
    if sexo == 'F' and idade < 20:
        muie += 1
    
    cont += idade
    print()

print()
print(f'A média de idades dessas pessoas é: {cont/4} anos')
print(f'O nome do homem mais velho é: {nomeh} e ele tem {homivelho} anos')
print(f'{muie} mulheres têm menos de 20 anos.')

linha()
