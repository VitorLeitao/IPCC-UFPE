# Leitura das infos iniciais
num_jogadas01 = int(input())
nome_01 = input()
nome_02 = input()
nome_03 = input()

# Variaveis acumuladoras
soma_01 = 0
soma_02 = 0
soma_03 = 0

contador = 0 # Contador
while contador < num_jogadas01:
    jogada_01 = int(input())
    jogada_02 = int(input())
    jogada_03 = int(input())
    soma_01 += jogada_01
    soma_02 += jogada_02
    soma_03 += jogada_03
    if soma_01 >= 200 or soma_02 >= 200 or soma_03 >= 200:
        contador = num_jogadas01
    contador += 1

# Colocando em ordem de maiores pontuações
nome_maximo = nome_01
pontuacao_maxima = soma_01

# Comparando pontuações com pontuação 2
if soma_02 > pontuacao_maxima:
    pontuacao_media = pontuacao_maxima
    nome_medio = nome_maximo
    nome_maximo = nome_02
    pontuacao_maxima = soma_02
else:
    pontuacao_media = soma_02
    nome_medio = nome_02

if soma_03 > pontuacao_maxima:
    indicado_paredao = nome_medio
    pontuacao_paredao = pontuacao_media
    pontuacao_media = pontuacao_maxima
    nome_medio = nome_maximo
    nome_maximo = nome_03
    pontuacao_maxima = soma_03
elif soma_03 > pontuacao_media:
    indicado_paredao = nome_medio
    pontuacao_paredao = pontuacao_media
    pontuacao_media = soma_03
    nome_medio = nome_03
else:
    indicado_paredao = nome_03
    pontuacao_paredao = soma_03


print(f'{indicado_paredao} ja esta confirmado no paredao')
print(f'1° - {nome_maximo}\n2° - {nome_medio}')

# Novas variaveis acumuladoras
soma_01 = 0
soma_02 = 0

# Lendo numero de jogadas da 2° rodada
num_jogadas02 = int(input())

for c in range(0, num_jogadas02):
    jogada_01 = int(input())
    jogada_02 = int(input())
    soma_01 += jogada_01
    soma_02 += jogada_02

if soma_01 < soma_02:
    segundo_paredao = nome_maximo
else:
    segundo_paredao = nome_medio

print(f'Nosso paredao sera entre {segundo_paredao} e {indicado_paredao}')







