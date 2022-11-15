nome = input()
vida = int(input())
def combate(jogador, inimigo, qtd_inimigo):
    vida_jogador = int(vida)
    dano_jogador = int(jogador[0])
    custo = int(jogador[1])
    armazen = int(jogador[2])
    dano_mostro = int(inimigo[0])
    vida_monstro = int(inimigo[1])
    vida_total_monstro = vida_monstro * qtd_inimigo
    while (qtd_inimigo > 0) and (vida_jogador > 0):
        dano_inimigo_total = dano_mostro * qtd_inimigo
        # JOGADOR ATANDO MONSTRO
        if armazen >= custo:
            vida_total_monstro -= dano_jogador
            if vida_monstro == dano_jogador:
                qtd_inimigo -= 1
            elif dano_jogador > vida_monstro:
                qtd_inimigo -= (dano_jogador // vida_monstro)
                vida_total_monstro -= (dano_jogador - (dano_jogador // vida_monstro))
            else:
                vida_total_monstro -= dano_jogador
            armazen -= custo
        else:
            vida_jogador = 0
        
        # MONSTRO ATACANDO JOGADOR
        dano_inimigo_total = dano_mostro * qtd_inimigo
        vida_jogador -= dano_mostro
    
    if vida_jogador > 0:
        return 'vivo'
    else:
        return 'morto'

def qual_inimigo(nome_inimigo):
    if nome_inimigo == 'Lurker':
        dano = 1
        vida = 2
    elif nome_inimigo == 'Nosalis':
        dano = 2
        vida = 5
    elif nome_inimigo == 'Spiderbug':
        dano = 4
        vida = 1
    elif nome_inimigo == 'Watcher':
        dano = 5
        vida = 4
    elif nome_inimigo == 'Librarian':
        dano = 10
        vida = 20
    return dano, vida
    
def qual_arma(nome_arma, qtd_cartucho):
    if nome_arma == 'Revolver':
        dano = 2
        municao_gasta = 1
        balas_total = qtd_cartucho * 6
    elif nome_arma == 'Bastard':
        dano = 3
        municao_gasta = 15
        balas_total = qtd_cartucho * 30
    elif nome_arma == 'Duplet':
        dano = 5
        municao_gasta = 2
        balas_total = qtd_cartucho * 2
    elif nome_arma == 'VSV':
        dano = 12
        municao_gasta = 3
        balas_total = qtd_cartucho * 21
    elif nome_arma == 'Kalash':
        dano = 20
        municao_gasta = 5
        balas_total = qtd_cartucho * 30
    return dano, municao_gasta, balas_total
continuar = 'sim'
contador = 0
while continuar == 'sim':
    if contador == 0:
        contador = 1
        partida = input()
        chegada = input()
        if partida == chegada:
            print(f'{nome} terminou sua jornada em {chegada}')
            continuar = 'nao'
        equip = input()
        arma = equip.split()[0]
        bala = int(equip.split()[2])
        infos_jogador = qual_arma(arma, bala)
        evento = input()
        if evento.split()[0] == 'combate':
            nome_inim = evento.split()[1]
            quantidade_inimigos = evento.split()[-1]
            infos_inimigo = qual_inimigo(nome_inim)
            status = combate(infos_jogador, infos_inimigo)
            if status == 'morto':
                print(f'{nome} lutou bravamente, mas o metrô o derrotou a caminho de {chegada}')
    else:
        chegada_provisoria = input()
        evento = input()
        if (chegada_provisoria == chegada) and (status == 'vivo'):
            contador = 0
            ...

