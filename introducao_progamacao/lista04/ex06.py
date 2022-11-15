def mudar_posicao_jason(matriz_atual, posicao_jason_x, posicao_jason_y):
    # Achando a posicao de V
    x = 0
    y = 0
    for c in matriz:
        if 'V' in c:
            x = c.index('V')
            break
        y += 1
    if posicao_jason_x == x:
        if y > posicao_jason_y:
            matriz[posicao_jason_y + 1][posicao_jason_x] = '-'
            matriz[posicao_jason_y][posicao_jason_x], matriz[posicao_jason_y + 1][posicao_jason_x] = matriz[posicao_jason_y + 1][posicao_jason_x], matriz[posicao_jason_y][posicao_jason_x]
            posicao_jason_y += 1
        else:
            matriz[posicao_jason_y - 1][posicao_jason_x] = '-'
            matriz[posicao_jason_y - 1][posicao_jason_x], matriz[posicao_jason_y][posicao_jason_x] = matriz[posicao_jason_y][posicao_jason_x], matriz[posicao_jason_y - 1][posicao_jason_x]
            posicao_jason_y -= 1
    else:
        if x > posicao_jason_x:
            matriz[posicao_jason_y][posicao_jason_x + 1] = '-'
            matriz[posicao_jason_y][posicao_jason_x], matriz[posicao_jason_y][posicao_jason_x + 1] = matriz[posicao_jason_y][posicao_jason_x + 1], matriz[posicao_jason_y][posicao_jason_x]
            posicao_jason_x += 1
        else:
            matriz[posicao_jason_y][posicao_jason_x - 1] = '-'
            matriz[posicao_jason_y][posicao_jason_x], matriz[posicao_jason_y][posicao_jason_x - 1] = matriz[posicao_jason_y][posicao_jason_x - 1], matriz[posicao_jason_y][posicao_jason_x]
            posicao_jason_x -= 1
    return posicao_jason_x, posicao_jason_y

def mudar_posicao_voce(matriz_atual, voce_x, voce_y, j_x, j_y, g_x, g_y, c_x, c_y):
    if not ('G' in matriz[g_y]):
        if voce_x == c_x:
            if c_y > voce_y:
                matriz[voce_y+1][voce_x]  = '-'
                matriz[voce_y][voce_x], matriz[voce_y+1][voce_x] = matriz[voce_y+1][voce_x], matriz[voce_y][voce_x]
                voce_y += 1
            else:
                matriz[voce_y-1][voce_x] = '-'
                matriz[voce_y][voce_x], matriz[voce_y-1][voce_x] = matriz[voce_y-1][voce_x], matriz[voce_y][voce_x]
                voce_y -= 1
        else:
            if c_x > voce_x:
                matriz[voce_y][voce_x+1] = '-'
                matriz[voce_y][voce_x], matriz[voce_y][voce_x+1] = matriz[voce_y][voce_x + 1], matriz[voce_y][voce_x]
                voce_x += 1
            else:
                matriz[voce_y][voce_x-1] = '-'
                matriz[voce_y][voce_x], matriz[voce_y][voce_x-1] = matriz[voce_y][voce_x - 1], matriz[voce_y][voce_x]
                voce_x -= 1
    else:
        if voce_x == g_x:
            if g_y > voce_y:
                matriz[voce_y+1][voce_x] = '-'
                matriz[voce_y][voce_x], matriz[voce_y+1][voce_x] = matriz[voce_y+1][voce_x], matriz[voce_y][voce_x]
                voce_y += 1
            else:
                matriz[voce_y-1][voce_x] = '-'
                matriz[voce_y][voce_x], matriz[voce_y-1][voce_x] = matriz[voce_y-1][voce_x], matriz[voce_y][voce_x]
                voce_y -= 1
        else:
            if g_x > voce_x:
                matriz[voce_y][voce_x+1] = '-'
                matriz[voce_y][voce_x], matriz[voce_y][voce_x+1] = matriz[voce_y][voce_x + 1], matriz[voce_y][voce_x]
                voce_x += 1
            else:
                matriz[voce_y][voce_x-1] = '-'
                matriz[voce_y][voce_x], matriz[voce_y][voce_x-1] = matriz[voce_y][voce_x - 1], matriz[voce_y][voce_x]
                voce_x -= 1
    return voce_x, voce_y

matriz = [
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-']
]


sua_posicao_y = int(input())
sua_posicao_x = int(input())
matriz[sua_posicao_y][sua_posicao_x] = 'V'
jason_y = int(input())
jason_x= int(input())
matriz[jason_y][jason_x] = 'J'
gasolina_y = int(input())
gasolina_x = int(input())
matriz[gasolina_y][gasolina_x] = 'G'
carro_y = int(input())
carro_x = int(input())
matriz[carro_y][carro_x] = 'C'

var = 0
continuar = True
acabou = 'nao'
while acabou == 'nao':
    a = mudar_posicao_jason(matriz, jason_x, jason_y)
    jason_x = int(a[0])
    jason_y = int(a[-1])
    # VENDO SE O JASON PEGOU VOCE
    if (jason_x == sua_posicao_x) and (jason_y == sua_posicao_y):
        frase = 'Oh nao, o Jason me pegou, F total!'
        acabou = 'sim'
    if (var == 0) and (acabou == 'nao'):
        b = mudar_posicao_voce(matriz, sua_posicao_x, sua_posicao_y, jason_x, jason_y, gasolina_x, gasolina_y, carro_x, carro_y)
        sua_posicao_x = int(b[0])
        sua_posicao_y = int(b[-1])
    else:
        var -= 1
        continuar = False
    # VENDO SE VOCE CHEGOU NA GASOLINA
    if (sua_posicao_x == gasolina_x) and (sua_posicao_y == gasolina_y) and (continuar == True):
        var = 1
        frase = 'Deu bom! Peguei a Gasolina nessa rodada.'
    # VENDO SE VOCE CHEGOU NO CARRO
    elif (sua_posicao_x == carro_x) and (sua_posicao_y == carro_y):
        frase = 'Consegui chegar no carro, agora e so ligar e fugir daqui!'
        acabou = 'sim'
    # Caso nao chegue em nada
    else:
        if acabou == 'nao':
            frase = 'Nao peguei nenhum objeto nessa rodada :('
    # PRINTANDO A MATRIZ
    for i in matriz:
        contador = 0
        for k in i:
            contador += 1
            if contador == 6:
                print(f'{k}')
            else:
                print(f'{k} ',end='')
    print(frase)
    # FAZENDO A DISTANCIA ENTRE JASON E VOCE
    if acabou == 'nao':
        distancia = int(((jason_x - sua_posicao_x)**2 + (jason_y - sua_posicao_y)**2) ** (1/2))
        if distancia <= 3:
            print('E melhor correr, o Jason vai me pegar!')
        elif 3 < distancia <= 4:
            print('Consigo ver o Jason daqui, preciso apressar o passo!')
        else:
            print('Ufa, o Jason ainda esta longe, mas nao posso diminuir o ritmo.')
        print()