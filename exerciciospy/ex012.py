# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto? R$'))
desconto = (preco * 5 / 100)
vf = preco - desconto
print(f'O valor com o desconto fica {vf:.2f}R$')