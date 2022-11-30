# Rating da Beth Harmon
rating_beth = int(input())
rating_adversario = int(input())
resultado_partida = input()
if resultado_partida == 'vitoria' or resultado_partida == 'empate' or resultado_partida == 'derrota':
    if resultado_partida == 'vitoria':
        ponto = 1
    elif resultado_partida == 'empate':
        ponto = 0.5
    else:
        ponto = 0

    estatistica = 1 / (1 + (10 ** ((rating_adversario - rating_beth) / 400)))
    novo_rating = rating_beth + (40 * (ponto - estatistica))
    novo_rating = int(novo_rating)
    print(f'O novo rating da Beth Harmon é {novo_rating}')
else:
    print('Resultado da partida invalido')