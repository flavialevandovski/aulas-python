# Exercício 8
# calcule o valor final de um produto, considerando o preço original e o percentual de desconto. Exiba o valor do desconto e o preço final com desconto.
# Peça ao usuário o preço original e o percentual de desconto.
# considere tambem se o pagamento for a vista, aplique um desconto adicional de 5% sobre o preço com desconto.

preco_produto= float(input('Qual o valor do produto? '))
percentual_de_desconto= int(input('Qual é o percentual de desconto pro produto? '))
a_vista= input('O pagamento é á vista? (S/N)')

valor_do_desconto= preco_produto * (percentual_de_desconto/100)
preco_com_desconto= preco_produto - valor_do_desconto

if a_vista.upper() == 'S':
    desconto_adicional= preco_com_desconto * (5/100)
    preco_com_desconto_adicional= preco_com_desconto - desconto_adicional
    print(f'O preço final do produto com desconto é de:{preco_com_desconto_adicional} ')
else:
    print(f'O preço final com desconto é de {preco_com_desconto}')

