# contando quantos "a"s tem no final (com recursão)
def contar_final(palavra, cont, contador_a):
    if palavra[-1] != 'a':
        return contador_a
    contador_a += 1
    return contar_final(palavra[0:cont], cont -1, contador_a)

# contando quantos "a"s tem no começo(sem recursão)
def contar_comeco(palavra, contador):
    for c in palavra:
        if c == 'a':
            contador += 1
        elif c != 'a':
            break
    return contador
# ADD quantidade de "a"s no começo
def add(palavra, contador_comeco, contador_final):
    contador = contador_final - contador_comeco
    if contador > 0:
        for c in range(contador):
            palavra.insert(0, 'a')
    return palavra

# Função para ver se é um palindromo(sem recursão)
def palindromo(palavra):
    nova_palavra = []
    for c in range(len(palavra)-1,-1,-1):
        nova_palavra.append(palavra[c])
    if nova_palavra == palavra:
        return 'sim'
    else:
        return 'nao'
# Input
numero = int(input())
contador = 0
for c in range(numero):
    frase = input()
    frase = list(frase)
    if 'a' in frase:
        # vendo se a frase é composta apenas por a
        cont = 0
        for c in frase:
            if c == 'a':
                cont += 1      
        if cont == len(frase): # Caso seja so A
            contador += 1
        # Caso nao seja
        else:
            a_comeco = contar_comeco(frase, 0)
            a_final = contar_final(frase, len(frase) - 1, 0)
            frase_final = add(frase, a_comeco, a_final)
            resultado = palindromo(frase)
            if resultado == 'sim':
                contador += 1
    else:
        resultado = palindromo(frase)
        if resultado == 'sim':
            contador += 1
if contador == numero:
    print('ACHEI!!! Peach, estou a caminho.')
else:
    print('Essa não!!! Estou na direção errada.')

