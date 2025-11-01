# Exercício 6
# realize o calculo da media final de um aluno, considerando que o aluno tem 3 notas, a primeira com peso 2, a segunda com peso 3 e a terceira com peso 5.

nota1= float(input('Digite a primeira nota com peso 2: '))
nota2= float(input('Digite a segunda nota com peso 3: '))
nota3= float(input('Digite a terceira nota com peso 5: '))

media_final= ((nota1*2) + (nota2*3) + (nota3*5)) / 3
print(f'A média das notas é {media_final}')