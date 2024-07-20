# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

tc = float(input('Informe a temperatura: ºC '))

tf = ((9 * tc) / 5) + 32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(tc, tf))
