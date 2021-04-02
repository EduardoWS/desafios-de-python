print()
print('=' * 40)
mat = float(input('Nota de matemática: '))
pt = float(input('Nota de português: '))
bio = float(input('Nota de biologia: '))
fis = float(input('Nota de física: '))
qui = float(input('Nota de química: '))
soc = float(input('Nota de sociologia: '))
his = float(input('Nota de história: '))
geo = float(input('Nota de geografia: '))
ing = float(input('Nota de inglês: '))
edf = float(input('Nota de educação físca: '))
fil = float(input('Nota de filosofia: '))

m = (mat + pt + bio + fis + qui + soc + his + geo + ing + edf + fil) / 11

print()
print(f'Média: {m:.1f}')
print('=' * 40)
