'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
 o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

mais18 = homem = mulher20 = 0

while True:

    print('-' * 30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-' * 30)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    print('-' * 30)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher20 += 1
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher20} com menos de 20 anos')
print('-' * 30)
