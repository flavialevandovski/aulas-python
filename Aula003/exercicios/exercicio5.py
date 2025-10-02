#--- Exercicio 5  - Variávies e impressão com interpolacão de string

#--- Imprima os dados de 5 papeis cotatos na bolsa de valores de SP
#--- Os dados dos papeis devem estar em variáveis
#--- Papel: Nome, Tipo, Cotação Atual e Valores Min e Max do dia 
#--- A tela deve conter cabeçalho e rodapé 

barra='='*55
print(barra)
print('\tBOLSA DE VALORES - COTAÇAO DE PAPEIS')
print(barra)
# 5 bolsas de papeis cotados
papel1_nome= 'PETR4'
papel1_tipo= 'Ação'
papel1_cotacao_atual= 28.50
papel1_min= 28.20
papel1_max= 29.00

papel2_nome= 'VALE3'
papel2_tipo= 'Ação'
papel2_cotação_atual= 95.30
papel2_min= 94.80
papel2_max= 96.00

papel3_nome= 'ITUB4'
papel3_tipo= 'Ação'
papel3_cotação_atual= 27.10
papel3_min= 26.90
papel3_max= 27.50

papel4_nome= 'BBDC4'
papel4_tipo= 'Ação'
papel4_cotação_atual= 22.80
papel4_min= 22.50
papel4_max= 23.10

papel5_nome= 'ABEV3'
papel5_tipo= 'Ação'
papel5_cotação_atual= 14.20
papel5_min= 14.00
papel5_max= 14.50

print(f'1. {papel1_nome}  Tipo: {papel1_tipo}  Cotação Atual: {papel1_cotacao_atual}  Min: {papel1_min}  Max:{papel1_max}')
print(f'2. {papel2_nome}  Tipo: {papel2_tipo}  Cotaçao Atual: {papel2_cotação_atual}  Min: {papel2_min}  Max: {papel2_max}')
print(f'3. {papel3_nome}  Tipo: {papel3_tipo}  Cotação Atual: {papel3_cotação_atual}  Min: {papel3_min}  Max: {papel3_max}')
print(f'4. {papel4_nome}  Tipo: {papel4_tipo}  Cotação Atual: {papel4_cotação_atual}  Min: {papel4_min}  Max: {papel4_max}')
print(f'5. {papel5_nome}  Tipo: {papel5_tipo}  Cotação Atual: {papel5_cotação_atual}  Min: {papel5_min}  Max: {papel5_max}')
print(barra)
print('\tCotação de hoje: ENCERRADA')
print(barra)