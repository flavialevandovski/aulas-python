#--- Exercicio 4  - Variávies e impressão com interpolacão de string

#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- Entre os dois pontos deve conter no minimo 10 pontos de parada
#--- Cada item deve conter data, hora e descrição
#--- O itineário deve conter cabeçalho com o título da viagem
#--- Os dados de cada ponto devem estar em variáveis
#--- Deve ser usado os caracteres de tabulação, quebra de linha e a função Format()
barra_cabecalho= "="*10
estrela_cabecalho2='*'*10
print('\n'*1)
print(barra_cabecalho,'itinerário viagem de férias',barra_cabecalho)
print('\n'*1)
print(estrela_cabecalho2,'dados do itinerário',estrela_cabecalho2)
print('\n'*1)
#ponto de partida
p1_data='02/10/2025'
p1_hora='08:00'
p1_desc='Saída de Blumenau-SC'
#pontos de parada
p2_data='02/10/2025' 
p2_hora='10:30'
p2_desc='parada em Joinville-SC para tomar café da manhã'

p3_data='02/10/2025'
p3_hora='12:00'
p3_desc='parada em Curitiba-PR para almoçar'

p4_data='02/10/2025'
p4_hora='14:30'
p4_desc='parada em Londrina-PR para descanso'

p5_data='02/10/2025'
p5_hora='17:00'
p5_desc='parada em Maringá-PR, lanche rápido'

p6_data='02/10/2025'
p6_hora='19:30'
p6_desc='parada em Uberlandia-MG para jantar'

p7_data='02/10/2025'
p7_hora='21:00'
p7_desc='parada em Patos de Minas-MG pra descansar'

p8_data='03/10/2025'
p8_hora='06:30'
p8_desc='parada em Araxá-MG, tomar café da manhã'

p9_data='03/10/2025'
p9_hora='09:00'
p9_desc='parada em Sete Lagoas-MG em  posto de combustivel'

p10_data='03/10/2025'
p10_hora='12:00'
p10_desc='parada em Confins-MG para almoço'
#destino
p11_data='03/10/2025'
p11_hora='13:00'
p11_desc='chegada em Belo Horizonte-MG'

print('Ponto de Partida:\n\tData: {0}\tHora: {1}\tDescrição: {2}\n'.format(p1_data, p1_hora, p1_desc))
print('\n'*1)
print('ponstos de parada:')
print('\tPonto 2:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p2_data,p2_hora,p2_desc))
print('\tPonto 3:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p3_data,p3_hora,p3_desc))
print('\tponto 4:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p4_data,p4_hora,p4_desc))
print('\tponto 5:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p5_data,p5_hora,p5_desc))
print('\tponto 6:\tData: {0}\tHora: {1}\tDsecrição: {2}'.format(p6_data,p6_hora,p6_desc))
print('\tponto 7:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p7_data,p7_hora,p7_desc))
print('\tponto 8:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p8_data,p8_hora,p8_desc))
print('\tponto 9:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p9_data,p9_hora,p9_desc))
print('\tponto 10:\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p10_data,p10_hora,p10_desc))
print('\n'*1)
print('ponto de chegada:')
print('\tData: {0}\tHora: {1}\tDescrição: {2}'.format(p11_data,p11_hora,p11_desc))
print('\n'*1)