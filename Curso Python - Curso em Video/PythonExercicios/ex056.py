'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.'''

sidade = 0
mediaidade = 0
maioridade = 0
maiornome = ''
fcont = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    sidade += idade
    if sexo in 'Mn' and p==1:
        maioridade = idade
        maiornome = nome
    elif sexo in 'Mn' and maioridade < idade:
        maioridade = idade
        maiornome = nome
    elif sexo in 'Ff' and idade < 20:
        fcont += 1

mediaidade = sidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, maiornome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(fcont))
