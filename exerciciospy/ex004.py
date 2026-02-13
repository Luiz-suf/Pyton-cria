# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçõess possiveis sobre ele.

a = input('Digite Algo:')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É númerico? {a.isnumeric()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'é alfanumerico? {a.isalnum()}')
print(f'está em maiuscula? {a.isupper()}')
print(f'está em minusculo? {a.islower()}')
print(f'está capitalizada? {a.istitle()}')