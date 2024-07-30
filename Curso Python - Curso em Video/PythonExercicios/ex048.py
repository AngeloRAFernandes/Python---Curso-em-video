''' Faça um programa que calcule a soma entre todos os números IMPARES que são
 múltiplos de três e que se encontram no intervalo de 1 até 500.'''

cont = 0
total = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        total += n
        cont += 1

print('A soma de todos os {} valores solicitados é {}'.format(cont, total))
