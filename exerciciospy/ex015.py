#Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa 60 reais por dia e 0.15 centavos por quilômetro rodado.
dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos kms rodados '))
valor = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${valor:.2f}')