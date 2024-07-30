'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
 programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

n = soma = cont = 0
escolha = ''

while escolha != 'N':

    n = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    soma += n

    if cont == 0:
        menor = maior = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

    cont += 1

media = soma / cont

print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
