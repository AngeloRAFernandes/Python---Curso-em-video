lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
# Tuplas são imutáveis
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('=' * 30)
print(lanche)
print(sorted(lanche))
print('=' * 30)
a = (2, 5, 4)
b = 5, 8, 1, 2
c = a + b
print(c)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(4))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
print(pessoa)
