'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

op = 0
while op != 5:
    op = int(input('Escolha uma das opções abaixo:\n'
                   '[ 1 ] Somar\n'
                   '[ 2 ] Multiplicar\n'
                   '[ 3 ] Maior\n'
                   '[ 4 ] Novos números\n'
                   '[ 5 ] Sair do programa\n'
                   'Qual é a sua opção? '))

    if 0 < op < 5 :
        if op == 1:
            soma = n1 + n2
            print('{} + {} = {}'.format(n1, n2, soma))

        elif op == 2:
            multiplicar = n1 * n2
            print('{} X {} = {}'.format(n1, n2, multiplicar))

        elif op == 3:
            if n1 < n2:
                print('O maior é {}'.format(n2))
            elif n1 > n2:
                print('O maior é {}'.format(n1))
            else:
                print('Não há maior, os dois são iguais.')

        elif op == 4:
            print('Digite novamente os valores')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))

    elif op > 5:
        print('Opção invalida, digite novamente:')
    else:
        print('Desligando o sistema...')

    print('=-=' * 10)
    sleep(1.5)
