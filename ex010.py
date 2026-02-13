# Crie um programa que leia quanto dinheiro  uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = 5.22
conversao = float(real/dolar)
print(f'Com R${real:.2f} voce pode comprar US${conversao:.2f}')