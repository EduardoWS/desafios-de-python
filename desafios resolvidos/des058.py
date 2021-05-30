import random

print('=' * 40)
print('JOGO DE ADIVINHAÇÃO' .center(40, ' '))
print('=' * 40)
cont = 1
while True:
    num_pc = random.randint(1, 5)
    escolha = int(input('Escolha um número de 1 a 5: '))
    
    if escolha == num_pc:
        print(f'Você venceu! {cont} tentativa(s)')
        perg = int(input('Digite 1 se quiser continuar e 2 se quiser parar: '))
        if perg == 2:
            break
    else:
        print('Você perdeu!')
        print(f'O número certo era {num_pc}')
        perg = int(input('Digite 1 se quiser continuar e 2 se quiser parar: '))
        cont += 1
        if perg == 2:
            break
    print()
print('Fim de jogo!')
