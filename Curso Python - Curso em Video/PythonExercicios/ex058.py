'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
 foram necessários para vencer.'''

from random import randint

# Faz o sorteio do número
computador = randint(0, 10)

# Cabeçalho
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

'''
jogador = 11
tentativas = 0
while jogador != computador:
# Jogador tenta adivinhar
    jogador = int(input('Em que número eu pensei? '))
    tentativas += 1

    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
'''

acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print('PARABENS! Você acertou com {} tentativas'.format(tentativas))
