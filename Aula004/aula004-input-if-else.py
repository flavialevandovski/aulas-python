#--- Aula 4  13-10-2025
#--- Input, Estruturas de decisão e Operadores Lógicos


# Exemplo 1: Verifica se o nome contém a letra "A"
nome = input("Digite seu nome: ")
nome = nome.upper() # Converte o nome para maiúsculas
#nome = nome.lower() # Converte o nome para minúsculas

if 'A' in nome: #True ou False
    print("Seu nome contém a letra A.")
else:
    print("Seu nome não contém a letra A.")

# Exemplo 2: Verifica se a idade está entre 13 e 19 (adolescente)
idade = int(input("Digite sua idade: "))

if idade >= 13 and idade <= 19:
    print("Você é um adolescente.")
else:
    print("Você não é um adolescente.")

# Exemplo 3: Verifica se um número está fora do intervalo de 10 a 20
numero = int(input("Digite um número: "))
if numero < 10 or numero > 20:
    print("O número está fora do intervalo de 10 a 20.")
else:
    print("O número está dentro do intervalo de 10 a 20.")
# Exemplo 4: Mostra o maior entre três números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior_numero = n1  # Assume que n1 é o maior inicialmente
if n2 > maior_numero:
    maior_numero = n2
if n3 > maior_numero:
    maior_numero = n3
print("O maior número é:", maior_numero)

# Exemplo 5: Verifica se dois números são pares ou ímpares
# tem que ser divisivel por 2 com resto 0, ou seja, divisão exata
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

r1 = numero1 % 2
r2 = numero2 % 2

if r1 == 0:
    print(f'O numero {numero1} é par')
else:
    print(f'O numero {numero1} é impar')

# chegagem diferente para exemplo (poderia ser igual)
if r2 != 0:
    print(f'O numero {numero2} é impar')
else:
    print(f'O numero {numero2} é par')
