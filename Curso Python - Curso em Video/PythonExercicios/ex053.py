'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
 desconsiderando os espaços. Exemplos de palíndromos:
 APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)

# metodo 1 com uso de FOR
#inverso = ''
#for letra in range(len(junto)-1, -1, -1):
#    inverso += junto[letra]

# metodo 2 sem FOR
inverso = junto[::-1]

print('A frase {} ao inverso é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palíndromo!')
