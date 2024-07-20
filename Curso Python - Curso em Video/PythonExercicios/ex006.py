# Crie um algoritimo que leia um número e mostre o seu
# dobro, triplo e a raiz quadrada.

n = int(input('Digite um número: '))

print('Você digitou {}\nSeu dobro é {}\nSeu triplo é {}\nSua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), pow(n,(1/2))))
