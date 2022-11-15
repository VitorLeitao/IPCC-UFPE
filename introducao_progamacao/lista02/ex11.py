vida_lucas = 100
vida_severino = 100
c = 0 # Contador 
while c < 12:
    acao_lucas = input()
    acao_severino = input()
    if c == 3:
        vida_lucas, vida_severino = vida_severino, vida_lucas
    elif c == 6:
        dano_extra_lucas = (dano_lucas_levou) + (dano_lucas_levou * 0.5) + (dano_lucas_levou * 0.25)
        dano_extra_severino = (dano_severino_levou) + (dano_severino_levou * 0.5) + (dano_severino_levou * 0.25)
        vida_lucas -= dano_extra_lucas
        vida_severino -= dano_extra_severino
    elif c == 9:
        if vida_lucas < vida_severino:
            vida_lucas = vida_severino
        else:
            vida_severino = vida_lucas
    else:
        # Possibilidades quando o primeiro esta atacando
        if acao_lucas == 'Golpe Rapido':
            if acao_severino == 'Golpe Rapido':
                dano_severino_levou = 12
                dano_lucas_levou = 12

            elif acao_severino == 'Bloqueio':
                dano_severino_levou = 6
                dano_lucas_levou = 0

            elif acao_severino == 'Esquivar':
               dano_severino_levou = 12
               dano_lucas_levou = 0

            elif acao_severino == 'Golpe Forte':
                dano_severino_levou = 12
                dano_lucas_levou = 25

        if acao_lucas == 'Golpe Forte':
            if acao_severino == 'Golpe Forte':
                dano_severino_levou = 0
                dano_lucas_levou = 0

            elif acao_severino == 'Bloqueio':
                dano_severino_levou = 20
                dano_lucas_levou = 0

            elif acao_severino == 'Esquivar':
                dano_severino_levou = 0
                dano_lucas_levou = 20

            elif acao_severino == 'Golpe Rapido':
                dano_severino_levou = 25
                dano_lucas_levou = 12

        # Possibilidades quando o jogador 2 esta atacando
        if acao_severino == 'Golpe Rapido':
            if acao_lucas == 'Golpe Rapido':
                dano_severino_levou = 12
                dano_lucas_levou = 12

            elif acao_lucas == 'Bloqueio':
                dano_lucas_levou = 6
                dano_severino_levou = 0

            elif acao_lucas == 'Esquivar':
               dano_lucas_levou = 12
               dano_severino_levou = 0

            elif acao_lucas == 'Golpe Forte':
                dano_lucas_levou = 12
                dano_severino_levou = 25

        if acao_severino == 'Golpe Forte':
            if acao_lucas == 'Golpe Forte':
                dano_lucas_levou = 0
                dano_severino_levou = 0

            elif acao_lucas == 'Bloqueio':
                dano_lucas_levou = 20
                dano_severino_levou = 0

            elif acao_lucas == 'Esquivar':
                dano_lucas_levou = 0
                dano_severino_levou = 20

            elif acao_lucas == 'Golpe Rapido':
                dano_lucas_levou = 25
                dano_severino_levou = 12
        vida_lucas -= dano_lucas_levou
        vida_severino -= dano_severino_levou

    if vida_lucas <= 0 or vida_severino <= 0:
        c = 12
    c += 1

if vida_lucas > vida_severino:
    print('Foi uma prova dificil, mas Lucas mostra como se faz e vence o BBCIn do 2021.2!!')
elif vida_severino > vida_lucas:
    print('Foi uma prova dificil, mas Severino mostra como se faz e vence o BBCIn do 2021.2!!')
else:
    print('Pela primeira vez na historia, ha um empate e ambos irao levar para casa o grande premio do BBCIn do 2021.2!!')

