"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = str(input('Digite o seu nome completo: ')).strip()

print('Analizando seu nome...')

print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
