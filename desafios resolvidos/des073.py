def linha():
    print()
    print('=' * 80)
    print()
linha()

times = ('Athletico-PR', 'Bragantino', 'Palmeiras', 'Fortaleza', 'Atlético-MG',
'Flamengo', 'Santos', 'Juventude', 'Internacional', 'Bahia',
'Atlético-GO', 'Ceará', 'Corinthians', 'Fluminense', 'América-MG',
'Sport', 'São Paulo', 'Cuiabá', 'Chapecoense', 'Grêmio')

print(f'''
1º {times[0]}
2º {times[1]}
3º {times[2]}
4º {times[3]}
5º {times[4]}''')

print()

print(f'''
17º {times[16]}
18º {times[17]}
19º {times[18]}
20º {times[19]}
''')
print()

print(f'São Paulo está na posição {times.index("São Paulo")+1}º')

print()
print()

for cont in range(0, len(times)):
    print(f'{cont+1}º {sorted(times)[cont]}')
linha()
