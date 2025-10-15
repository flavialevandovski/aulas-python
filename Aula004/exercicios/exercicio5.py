# Exercício 5
# Peça a idade do usuário para acesso a um serviço
# Só pode acessar se for maior de 18 anos.
# Se ele tiver idade entre 14 e 18 anos deve apresentar autorização dos pais. 
#  Neste caso pergunte se existe a autorização
idade=int(input('Qual a sua idade? '))
if idade >=14 and idade <=18:
    print('você deve apresentar autorização dos pais')
    autorizacao=input('pussui autorização?(s/n)')
    if autorizacao =='s':
        print('autorizado')
    else:
        print('não autorizado')
elif idade <14:
    print('não autorizado')
else:
    print('autorizado')
        

