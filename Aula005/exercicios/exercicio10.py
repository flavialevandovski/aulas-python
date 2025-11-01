# Exercício 10
# Peça ao usuário dois números inteiros, A e B.
# - Calcule e exiba o resultado de A elevado a B.
# - Em seguida, calcule e exiba o resultado da divisão de A por B, mas só realize a divisão se B for diferente de zero. Caso contrário, exiba uma mensagem de erro.
# - Por fim, exiba o resto da divisão de A por B, também apenas se B for diferente de zero.

numero_a= int(input('Digite um número inteiro: '))
numero_b= int(input('Digite um segundo número inteiro: '))
resultado_potencia= numero_a ** numero_b
print(f'{numero_a} elevado ao {numero_b} é o {resultado_potencia}')

if numero_b != 0:
    resultado_divisao = numero_a / numero_b
    resto = numero_a % numero_b
    print(f'A divisão de {numero_a} por {numero_b} é {resultado_divisao}')
    print(f'O resto da divisão de {numero_a} por {numero_b} é {resto}')
else:
    print('Erro: não é possível dividir por zero.')