#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula
nome= 'Flavia'
sobrenome= 'Levandovski'
cpf= '135.010.309-83'
rg= '7.948.616'
salario= 3000.03
print ('nome: {} \nsobrenome: {} \nCpf {} \nRg: {} \nsalario: {:.2f}\n'.format(nome,sobrenome,cpf,rg,salario))
