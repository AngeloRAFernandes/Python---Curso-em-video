#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

a = float(input('Digite o ângulo que você deseja: '))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, t))
