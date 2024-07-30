'''Escreva um programa em Python que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Digite um número inteiro: '))
menu = int(input('''Escolha uma das bases para conversão:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL
Sua opção: '''))

if menu == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))

elif menu == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))

elif menu == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))

else:
    print('Opção inválida. Tente novamente.')