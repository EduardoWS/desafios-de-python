import math
print()
print('=' * 40)
ang = int(input('Digite um ângulo qualquer: '))
convert = math.radians(ang)
sen = math.sin(convert)
cos = math.cos(convert)
tan = math.tan(convert)

print()
print(f'seno de {ang}° é {sen:.2f} \ncosseno de {ang}° é {cos:.2f} \ntangente de {ang}° é {tan:.2f}')
print()
print('=' * 40)
print()
