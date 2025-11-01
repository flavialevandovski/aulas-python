# Exercício 9
# calcule o percentual de valorização ou desvalorização de um produto.
#  Peça ao usuário o preço original e o preço atual do produto. Exiba o percentual com o símbolo %.
preco_original= float(input('Qual o valor original do produto? '))
preco_atual= float(input('qual o valor atual do produto? '))

diferenca= preco_atual - preco_original
print(f'A diferença do preço original {preco_original} pro atual {preco_atual} é {diferenca} ')

percentual= (diferenca / preco_original) * 100
if percentual >0:
    print(f' A valorização  foi de {percentual} %')
else:
    print(f'a desvalorização foi de {percentual} %')
