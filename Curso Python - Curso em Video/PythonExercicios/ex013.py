# Faça um algoritimo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salário: R$ '))

ns = s + (s * (15/100))

print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(s, ns))
