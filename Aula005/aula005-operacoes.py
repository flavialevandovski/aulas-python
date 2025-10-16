#--- Aula 5  16-10-2025
#--- Operações matemáticas com exemplos práticos

# Exemplo 1: Soma de três números
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

soma =  n1 + n2 + n3 # soma que diferente de uma concatenação(junção de strings)
print(f'A soma dos numeros é {soma}')


# Exemplo 2: Diferença absoluta entre dois números
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

diferenca = abs(n1 - n2)
print(f'A diferença entre os dois numeros é {diferenca}')

#Exemplo 3: Produto(*) e divisao (/)
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

if n2 == 0:
    print('O segundo numero nao pode ser zero')
else:        
    produto = n1 * n2
    divisao = n1 / n2

    print(f'O produto entre os dois numeros é {produto}')
    print(f'A divisao entre os dois numeros é {divisao}')

# Exemplo 4: Área de um retângulo (b*h)
base = int(input('Digite o valor da base do retângulo: '))
altura = int(input('Digite o valor da altura do retângulo: '))

area = base * altura
print(f'A area do retângulo é {area}')

# Exemplo 5: Divisão com verificação de zero (numerador/denominador)
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador: '))

if denominador == 0:
    print('O denominador nao pode ser zero')
else:
    divisao = numerador / denominador
    print(f'A divisao entre os dois numeros é {divisao}')

# Exemplo 6: Par ou ímpar usando módulo
n1 = int(input('Digite o primeiro numero: '))

if n1 % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')

#Exemplo 7: Quantos grupos completos consigo formar, validação de grupo > 0 (//)
n1 = int(input('Digite o numero de pessoas: '))
n2 = int(input('Digite quantas pessoas em cada grupo: '))

resultado = n1 // n2

print(f'{resultado} grupos completos')
#Exemplo 8: Exponenciação (**)
n1 = float(input('Digite a base: '))
n2 = float(input('Digite o expoente: '))

resultado = n1 ** n2
print(f'{n1} elevado a {n2} é {resultado}')

#Exemplo 9: Média aritmética de três valores
n1 = float(input('Digite o primeira nota: '))
n2 = float(input('Digite o segunda nota: '))
n3 = float(input('Digite o terceira nota: '))

media = (n1 + n2 + n3) / 3
print(f'A media das notas é {media}')

# Exemplo 10: Cálculo de desconto percentual, calculo do valor do desconto e preço final
valor_produto = float(input('Digite o valor do produto: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

desconto = valor_produto * (percentual_desconto / 100)

preco_final_com_desconto = valor_produto - desconto

print(preco_final_com_desconto)


