from pygame import mixer
print()
print('=' * 40)

mixer.init()
mixer.music.load("C:/Users/berse/OneDrive/Documentos/MeusProjetos/desafios-de-python/desafios resolvidos/Young Love.mp3")
mixer.music.play(-1)
input('Aperte qualquer tecla para parar: ')

print()
print('=' * 40)
print()
