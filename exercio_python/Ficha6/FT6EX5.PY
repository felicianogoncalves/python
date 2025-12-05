from areas import *

raio=float(input('Digite o raio para calcular o circulo'))
print(f'A área do circulo é {area_circulo(raio):.2f}')




base=float(input('Digite o a base do triangulo para calcular o tringulo'))
altura=float(input('Digite o a altura do triangulo para calcular o tringulo'))
print(f'A área do tringulo é {area_retangulo(base,altura):.2f}')




comprimento=float(input('Digite o a base do triangulo para calcular o retângulo'))
largura=float(input('Digite o a base do triangulo para calcular o retângulo'))
print(f'A área do retângulo é {area_retangulo(comprimento,largura):.2f}')
