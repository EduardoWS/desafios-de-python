def linha():
    print()
    print('=' * 80)
    print()
linha()

tupla = ('arroz', 'abelha', 'uva')

""" v = ()
for n in range(0, len(tupla)):
    
    if 'a' in tupla[n]:
        v += ('a',)
    if 'e' in tupla[n]:
        v += ('e',)
    if 'i' in tupla[n]:
        v += ('i',)
    if 'o' in tupla[n]:
        v += ('o',)
    if 'u' in tupla[n]:
        v += ('u',)
    
    
    v = str(v).replace('(', '')
    v = str(v).replace(')', '')
    v = str(v).replace("'", "")

    print(f'As vogais da palavra "{tupla[n]}" são: {v}')
    v = () """

v = []
for palavras in tupla:
    for letras in range(0, len(palavras)):

        if palavras[letras] in 'aeiou':
            v += [palavras[letras]]

    v = str(v).replace('[', '')
    v = str(v).replace(']', '')
    v = str(v).replace("'", "")
    print(f'As vogais da palavra "{palavras}" são: {v}')
    v = []

linha()
