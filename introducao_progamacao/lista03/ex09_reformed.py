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

erro = 'sim'
# TENTANDO ACHAR A CRUZ
for i in range(colunas):
    if erro == 'nao':
        break
    for c in range(linhas):
        if matriz[c][0][i] == '.':
            continue
        else:
            # Contando quantos * vao ter antes do "." para cada direção
            # esquerda
            contador_esquerda = 0
            for j in range((i + 1), colunas):
                if matriz[c][0][j] == '*':
                    contador_esquerda += 1
                else:
                    break
            # direita
            contador_direita = 0
            for k in range((i - 1), -1,-1):
                if matriz[c][0][k] == '*':
                    contador_direita += 1
                else:
                    break
            # Baixo
            contador_baixo = 0
            for l in range(c+1, linhas):
                if matriz[l][0][i] == '*':
                    contador_baixo += 1
                else:
                    break
            # Cima
            contador_cima = 0
            for m in range((c - 1), -1,-1):
                if matriz[m][0][i] == '*':
                    contador_cima += 1
                else:
                    break
            
            if contador_direita == contador_esquerda == contador_baixo == contador_cima:
                if contador_baixo == 1:
                    print('Nao foi um dos melhores, mas ta valendo...')
                    erro = 'nao'
                    break
                elif contador_baixo == 2:
                    print('Esta perfeito, quase peguei toda a premiaçao, UHUL!!')
                    erro = 'nao'
                    break
                elif contador_baixo == 3:
                    print('AEEEEW, ACHEI O PRECIOSO!!!!')
                    erro = 'nao'
                    break
                
            
if erro == 'sim':
    print('Puts, dessa vez nao tive sorte...')
