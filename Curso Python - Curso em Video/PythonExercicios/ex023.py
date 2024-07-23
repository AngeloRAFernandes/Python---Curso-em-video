"""Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados."""

print('Digite um número de 0 a 9999')
n = int(input('Informe seu número:'))
num = str(n)
print('Analisando o número {}'.format(num))

#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
