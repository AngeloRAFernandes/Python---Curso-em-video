"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""

while True:

    n = int(input('Quer ver a tabuada de qual valor? '))

    print('-'*30)
    if n < 0:
        print()
        break
    else:
        for tab in range(1, 11):
            print(f'{n} x {tab:2} = {n * tab}')
    print('-'*30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
