valores = input()
linhas = int(valores.split()[0])
colunas = int(valores.split()[-1])

# MONTANDO O ESQUELETO DA MATRIZ
matriz = []
for c in range(linhas):
    matriz.append([])

# PREENCHENDO A MATRIZ
contador = 0
for c in range(linhas):
    string = input()
    matriz[c].append(string)

# TENTANDO ACHAR A CRUZ
for c in range(linhas):
    if contador >= 1:
        break
    for i in range(colunas):
        if matriz[c][0][i] == '.':
            continue
        else: # ANALISANDO SE O * EM QUESTAO PODE SER PONTO CENTRAL
            # CASO TENHA ESPAÇO PRA UMA CRUZ DE 3
            try:
                if (matriz[c][0][(i-3):i] == '***') and (matriz[c][0][(i+1):(i+4)] == '***') and (matriz[c][0][i-4] == '.') and (matriz[c][0][i+4] == '.'):# vendo se tem *** no lado direito e esquerdo

                    if (matriz[c-1][0][i] == '*') and (matriz[c-2][0][i] == '*') and (matriz[c-3][0][i] == '*') and (matriz[c+1][0][i] == '*') and (matriz[c+2][0][i] == '*') and (matriz[c+3][0][i]) == '*' and (matriz[c+4][0][i] == '.') and (matriz[c-4][0][i] == '.'): # vendo se tem *** em cima e em baixo
                        print('AEEEEW, ACHEI O PRECIOSO!!!!')
                        contador += 1
                        break
            except:
                ...
            # CASO TENHA ESPAÇO PRA UMA CRUZ DE 2
            try:
                if (matriz[c][0][(i-2):i] == '**') and (matriz[c][0][(i+1):(i+3)] == '**') and (matriz[c][0][i-3] == '.') and (matriz[c][0][i+3] == '.'): # vendo se tem ** no lado direito e esquerdo
                    if (matriz[c-1][0][i] == '*') and (matriz[c-2][0][i] == '*') and (matriz[c+1][0][i] == '*') and (matriz[c+2][0][i] == '*') and (matriz[c-3][0][i] != '*') and (matriz[c+3][0][i] != '*'):# vendo se tem ** em cima e em baixo
                        print('Esta perfeito, quase peguei toda a premiaçao, UHUL!!')
                        contador += 1
                        break
            except:
                ...
            
            try:
                if (matriz[c][0][(i-1)] == '*') and (matriz[c][0][(i+1)] == '*') and (matriz[c][0][i-2] == '.') and (matriz[c][0][i+2] == '.'): # vendo se tem ** no lado direito e esquerdo
                    if (matriz[c-1][0][i] == '*') and (matriz[c+1][0][i] == '*') and (matriz[c-2][0][i] == '.') and (matriz[c+2][0][i] == '.'):# vendo se tem ** em cima e em baixo
                        print('Nao foi um dos melhores, mas ta valendo...')
                        contador += 1
                        break
            except:
                ...

if contador == 0:
    print('Puts, dessa vez nao tive sorte...')


