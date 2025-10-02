#--- Exercicio 2  - Variávies e impressão com interpolacão de string

#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format() para concatenar os números da opções, que devem ser números inteiros
#--- Alem das opções o menu deve conter um cabeçalho e um rodapé
#--- O cabeçalho e o rodapé devem ser impressos utilizando a multiplicação de caracters
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação
opt_cadastrar=1
opt_listar=2
opt_alterar=3
opt_deletar=4
barra_cabecalho= '='*10
print(barra_cabecalho,'cadastro de funcionarios',barra_cabecalho)
print('\n'*3)
print('\t{}-cadastrar'.format(opt_cadastrar))
print('\t{}-listar'.format(opt_listar))
print('\t{}-alterar'.format(opt_alterar))
print('\t{}-deletar'.format(opt_deletar))
print('\n'*3)
print(barra_cabecalho,'fim do menu',barra_cabecalho)

