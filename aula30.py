"""
CONSTANTE = Variáveis que não vão mudar
muitas condições no mesmo if(ruim)
    <-- contagem de complexidade(ruim)
sempre escritas em letra maiuscula
"""

velocidade =  61 # velocidade atual do carro
local_carro = 100 # quilometro atual na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_pass_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_pass_radar1


if velocidade_carro_pass_radar1:
    print('Você passou do limite de velocidade')

if carro_passou_radar1:
    print('Carro passou radar 1')


if carro_multado_radar1:
    print('Carro multado em radar 1')

