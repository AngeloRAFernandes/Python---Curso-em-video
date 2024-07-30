'''Elabore um programa que calcule o valor a ser pago por um produto, considerando
 o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS GUANABARA '))

preço = float(input('Preço das compras: R$ '))

menu = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if 1 <= menu <= 4:
    if menu == 1:
        total = preço - (preço * (10/100))
    elif menu == 2:
        total = preço - (preço * (5/100))
    elif menu == 3:
        total = preço
        print('Sua compra será parcelada em 2x de R${:.2f}'.format(total / 2))
    elif menu == 4:
        total = preço + (preço * (20/100))
        parcelas = int(input('Quantas parcelas? '))
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, total / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
else:
    print('Opção de pagamento invalida, Tente novamente!')
