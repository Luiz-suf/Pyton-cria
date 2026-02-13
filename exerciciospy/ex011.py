# Faça um program que leia a largura e a altura de uma parede em em metros, calcule a sua area e a quantidade de tinta necessaria para pint-la, sabendo que cada litro de tinta 
#  pinta uma area de 2m^2.
larg = float(input('Digite a largura da parede: '))
Alt = float(input('Digite a Altura da parede: '))
Area = larg * Alt
print(f'Sua parede tem dimensão de {larg} x {Alt} e sua area é {larg*Alt}m².')
tinta = Area/2
print(f'Para  pintar essa parede, voçê precisara de {tinta}l.')