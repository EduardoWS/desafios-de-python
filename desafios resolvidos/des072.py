def linha():
    print()
    print('=' * 80)
    print()
linha()
nums = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um valor de 1 a 20: '))

print(f'Número {nums[num-1]}')

linha()