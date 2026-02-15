#Faça um algoritimo que leia o salário de uma função e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o seu salário: R$'))
aumento =  salario * (15/100)
print(f'O aumento salarial será de {salario + aumento:.2f}R$')