def jogo(carta1, carta2):
    nome_1 = carta1.split('/')[0]
    pts_1 = int(carta1.split('/')[-1])
    pts_2 = int(carta2.split('/')[-1])
    nome_2 = carta2.split('/')[0]
    if pts_1 > pts_2:
        return nome_1, pts_1
    else:
        return nome_2, pts_2

cartas_luke = []
cartas_forca = []
for c in range(10):
    carta = input()
    if c < 5:
        cartas_luke.append(carta)
    else:
        cartas_forca.append(carta)

rounds_luke = 0
rounds_forca = 0
for c in range(5):
    vencedor = jogo(cartas_luke[c], cartas_forca[c])
    if vencedor[0] == cartas_luke[c].split('/')[0]:
        rounds_luke += 1
        print(f'Luke foi muito esperto, usou {vencedor[0]} e ganhou o {c+1}º round!')
        if rounds_luke >= 3:
            print('Luke Carter ganhou na batalha de cartas e avançou de fase na sua luta para conseguir sair da cabana!')
            break

    else:
        rounds_forca += 1
        print(f'Inscryption nao aliviou, usou {vencedor[0]} e venceu o {c+1}º round!')
        if rounds_forca >= 3:
            print('Luke Carter foi derrotado na batalha de cartas e sua alma permanecera na cabana para todo o sempre!')
            break



