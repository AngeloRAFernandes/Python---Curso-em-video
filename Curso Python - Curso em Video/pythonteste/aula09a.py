frase = 'Curso em Video Python'

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print()
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print()
print(len(frase))
print()


frase = '   Curso em Video Python   '

print(len(frase))
print(len(frase.strip()))
print()


frase = 'Curso em Video Python'

print(frase.replace('Python', 'Android'))
print()
print('Curso' in frase)
print()
print(frase.find('Curso'))
print(frase.find('Video'))
print(frase.find('video'))
print(frase.lower().find('video'))
print()

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])

