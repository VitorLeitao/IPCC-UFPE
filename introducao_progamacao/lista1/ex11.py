nome_1 = input()
vida_1 = int(input())
ataque_1 = int(input())
defesa_1 = int(input())
nome_2 = input()
vida_2 = int(input())
ataque_2 = int(input())
defesa_2 = int(input())

# ========================= ROUND 1 =====================================
golpe_round1 = input()
defesa_round1 = input()
if golpe_round1 == 'jab':
    if defesa_round1 == 'bloqueio':
        dano_recebido = (ataque_1 - ((ataque_1 * defesa_2) / 100))
        vida_2 -= dano_recebido
    if defesa_round1 == 'esquiva':
        ataque_2 = ataque_2 * 1.1
    if defesa_round1 == 'X':
        dano_recebido = ataque_1
        vida_2 -= dano_recebido

if golpe_round1 == 'direto':
    if defesa_round1 == 'bloqueio':
        dano_recebido = ((ataque_1 * 1.3) - ((ataque_1 * defesa_2) / 100))
        vida_2 -= dano_recebido
    if defesa_round1 == 'esquiva':
        ataque_2 = ataque_2 * 1.2
    if defesa_round1 == 'X':
        dano_recebido = ataque_1 * 1.4
        vida_2 -= dano_recebido

if vida_2 <= 0:
    print('Round 1')
    print(f'NOSSO CAMPEAO E {nome_1.upper()} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
else:
    # ============================== ROUND 2 ==========================
    golpe_round2 = input()
    defesa_round2 = input()
    if golpe_round2 == 'jab':
        if defesa_round2 == 'bloqueio':
            dano_recebido = (ataque_2 - ((ataque_2 * defesa_1) / 100))
            vida_1 -= dano_recebido
        if defesa_round2 == 'esquiva':
            ataque_1 = ataque_1 * 1.1
        if defesa_round2 == 'X':
            dano_recebido = ataque_2
            vida_1 -= dano_recebido

    if golpe_round2 == 'direto':
        if defesa_round2 == 'bloqueio':
            dano_recebido = ((ataque_2 * 1.3) - ((ataque_2 * defesa_1) / 100))
            vida_1 -= dano_recebido
        if defesa_round2 == 'esquiva':
            ataque_1 = ataque_1 * 1.2
        if defesa_round2 == 'X':
            dano_recebido = ataque_2 * 1.4
            vida_1 -= dano_recebido

    if vida_1 <= 0:
        print('Round 1')
        print('Round 2')
        print(f'NOSSO CAMPEAO E {nome_2.upper()}')
    else:
        # ===================ROUND 3========================
        golpe_round3 = input()
        defesa_round3 = input()

        if golpe_round3 == 'jab':
            if defesa_round3 == 'bloqueio':
                dano_recebido = (ataque_1 - ((ataque_1 * defesa_2) / 100))
                vida_2 -= dano_recebido
            if defesa_round3 == 'esquiva':
                ataque_2 = ataque_2 * 1.1
            if defesa_round3 == 'X':
                dano_recebido = ataque_1
                vida_2 -= dano_recebido

        if golpe_round3 == 'direto':
            if defesa_round3 == 'bloqueio':
                dano_recebido = ((ataque_1 * 1.3) - ((ataque_1 * defesa_2) / 100))
                vida_2 -= dano_recebido
            if defesa_round3 == 'esquiva':
                ataque_2 = ataque_2 * 1.2
            if defesa_round3 == 'X':
                dano_recebido = ataque_1 * 1.4
                vida_2 -= dano_recebido

        if vida_2 <= 0:
            print('Round 1')
            print('Round 2')
            print('Round 3')
            print(f'{nome_1.upper()} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO')
            print(f'NOSSO CAMPEAO E {nome_1.upper()}')
        else:
            print('Round 1')
            print('Round 2')
            print('Round 3')
            print(f'{nome_1.upper()} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO')
            print(f'NOSSO CAMPEAO E {nome_2.upper()}')

