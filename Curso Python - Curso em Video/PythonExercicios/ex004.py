# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

v = input('Digite algo: ')
print('O tipo primitivo desse valor é? {}'.format(type(v)))
print('O que você digitou foi: {}'.format(v))
print('Tem somente números? {}'.format(v.isnumeric()))
print('Tem somente letras? {}'.format(v.isalpha()))
print('Tem letras e/ou numeros? {}'.format(v.isalnum()))
print('Está escrito com letras maiúsculas? {}'.format(v.isupper()))
print('Está escrito com letras minúsculas? {}'.format(v.islower()))
print('Está escrita com letras minúsculas e maiúsculas? {}'.format(v.istitle()))
print('Pode ser impresso? {}'.format(v.isprintable()))
print('Só tem espaços? {}'.format(v.isspace()))
