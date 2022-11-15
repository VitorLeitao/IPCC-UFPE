def funcao(rodada, kill, vivos):
    resultado = int(((rodada * 10) + kill) - vivos)
    return resultado

numero_rodadas = int(input())
print('Haverá 10 inimigos na rodada 1')
for c in range(2, numero_rodadas + 1):
    infos = input()
    num_kills = int(infos.split('-')[0])
    num_vivos = int(infos.split('-')[-1])
    inimigos = funcao(c, num_kills, num_vivos)
    print(f'Haverá {inimigos} inimigos na rodada {c}')
