def mover(matriz, linha_l, coluna_l, num, situacao):
    # Caso-base2(link ganhou)
    if situacao == 'acabou':
        for c in range(len(matriz)):
            for i in range(len(matriz[c])):
                if i ==(len(matriz[c]) - 1):
                    print(f'{matriz[c][i]}')
                else:
                    print(f'{matriz[c][i]}',end='')
        print('Vamos embora daqui Princesa!!!')
        return 'ganhou'
    # Caso-base1 (linha perdeu)
    if (linha_l == -1) and (coluna_l == -1):
        print('HAHAHAHA você nunca irá resgatá-la, Link!!!')
        return 'perdeu'

    # Olhando em qual posição link vai
    if (not(linha_l == (num-1))) and ((matriz[linha_l + 1][coluna_l] == '.') or (matriz[linha_l + 1][coluna_l] == 'Z')): # Caso de pra ir ao sul
        if (matriz[linha_l + 1][coluna_l] == 'Z'):
            situacao = 'acabou'
        matriz[linha_l + 1][coluna_l] = 'L'
        linha_l += 1
        # Printando a matriz
        for c in range(len(matriz)):
            for i in range(len(matriz[c])):
                if i ==(len(matriz[c]) - 1):
                    print(f'{matriz[c][i]}')
                else:
                    print(f'{matriz[c][i]}',end='')
        print('Caminharei pelo Sul e certamente irei encontrar-te, Zelda')
        print()
    elif (not (coluna_l == (num-1))) and ((matriz[linha_l][coluna_l + 1]  == '.') or (matriz[linha_l][coluna_l + 1]  == 'Z')): # Caso seja leste
        if (matriz[linha_l][coluna_l + 1] == 'Z'):
            situacao = 'acabou'
        matriz[linha_l][coluna_l + 1] = 'L'
        coluna_l += 1
        # Printando a matriz
        for c in range(len(matriz)):
            for i in range(len(matriz[c])):
                if i ==(len(matriz[c]) - 1):
                    print(f'{matriz[c][i]}')
                else:
                    print(f'{matriz[c][i]}',end='')

        print('Caminharei pelo Leste e certamente irei encontrar-te, Zelda')
        print()
    elif (not linha_l == 0) and ((matriz[linha_l - 1][coluna_l] == '.') or (matriz[linha_l - 1][coluna_l] == 'Z')): # Caso seja norte
        if (matriz[linha_l - 1][coluna_l] == 'Z'):
            situacao = 'acabou'
        matriz[linha_l-1][coluna_l] = 'L'
        linha_l -= 1
        # Printando a matriz
        for c in range(len(matriz)):
            for i in range(len(matriz[c])):
                if i ==(len(matriz[c]) - 1):
                    print(f'{matriz[c][i]}')
                else:
                    print(f'{matriz[c][i]}',end='')
        print('Caminharei pelo Norte e certamente irei encontrar-te, Zelda')
        print()
    elif (not coluna_l == 0) and ((matriz[linha_l][coluna_l-1] == '.') or (matriz[linha_l][coluna_l-1] == 'Z')): # Caso seja oeste
        if (matriz[linha_l][coluna_l - 1] == 'Z'):
            situacao = 'acabou'
        matriz[linha_l][coluna_l - 1] = 'L'
        coluna_l -= 1
        # Printando a matriz
        for c in range(len(matriz)):
            for i in range(len(matriz[c])):
                if i ==(len(matriz[c]) - 1):
                    print(f'{matriz[c][i]}')
                else:
                    print(f'{matriz[c][i]}',end='')
        print('Caminharei pelo Oeste e certamente irei encontrar-te, Zelda')
        print()
    else:
        linha_l = -1
        coluna_l = -1
    return mover(matriz, linha_l, coluna_l, numero, situacao)
numero = int(input())
linha_link = int(input())
coluna_link = int(input())
matriz_inicial = []
# Preenchendo a matriz
for c in range(numero):
    linha = input()
    linha = list(linha)
    matriz_inicial.append(linha)

resultado = mover(matriz_inicial, linha_link, coluna_link, numero, 'nao acabou')


