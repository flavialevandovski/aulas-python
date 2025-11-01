# Exercício 7
# calcule a área de um círculo, pedindo ao usuário o valor do raio (A = π * r²). Use 3.14 para π.
raio= float(input('Digite o valor do raio: '))
pi= 3.14

area= pi * (raio**2)
print(f'A área do circulo é {area}')