#--- Exercicio 3  - Variávies e impressão com interpolacão de string

#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro
barra_cabecalho= '='*10
print('\n'*1)
print(barra_cabecalho,'livro',barra_cabecalho)
print('\n'*1)
titulo='transformando palavras em dinehiro'
ediçao= '1° edição'
autor='icáro de carvalho'
data='3 de fevereiro de 2020'
print(f'titulo= {titulo}')
print(f'ediçao= {ediçao}')
print(f'autor= {autor}')
print(f'data= {data}')
print('\n'*1)
print(barra_cabecalho,'paragrafo 1',barra_cabecalho)
print(''' Escrever é mais do que juntar palavras.\n É transmitir idéias de forma clara e persuasiva''')
print('\n'*1)
print(barra_cabecalho,'paragrafo 2',barra_cabecalho )
print(''' Quando aprendemos a usar as palavras como instrumento de valor,\n descobrimos que elas transforman a forma como as pessoas nos enxerga''')
print('\n'*1)