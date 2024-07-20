# Escreva um programa que leia um valor em metros e
# o exiba convertido em centimetros e milímetros.

m = float(input('Digite a distância em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a {}cm e {}mm'.format(m , cm, mm))
print('Tabela de medidas:\n {} km\n {} hm\n {} dam\n {} m\n {} dm\n {} cm\n {} mm'.format(km, hm, dam, m, dm, cm, mm))
