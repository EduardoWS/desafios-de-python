from random import randint
from time import sleep
print()
print('=' * 80)

vel = randint(65, 135)
multa = 7 * vel


print(' VRUUUUUUUMMMMMMMMMMMMMMMMM '.center(80))
sleep(2.5)
print()

print(f'Velocidade: {vel} km/h'.center(80))
print()

sleep(4)

if vel > 80:
    print('WOO-WII-WOO-WII-WOO-WII'.center(80))
    print()
    sleep(3)
    print('POLÍCIA! ENCOSTE O CARRO!!'.center(80))
    sleep(4)
    print('Você foi multado por ultrapassar o limite de velocidade'.center(80))
    print()
    print(f'Valor da multa: R${multa:.2f}'.center(80))

else:
    print('Sua velocidade está dentro do permitido!'.center(80))
    print('Continue dirigindo com cuidado!'.center(80))
print()
print('=' * 80)
print()
