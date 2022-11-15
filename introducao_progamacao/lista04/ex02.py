def tipo_frase(frase):
    # Vendo se é palindromo
    frase_sem_espacos = ''
    for i in range(len(frase)):
        letra = frase[i]
        if letra != ' ':
            frase_sem_espacos += letra
    frase_tras_frente = '' # frase de tras pra frente
    for k in range(len(frase)-1,-1,-1):
        letra = frase[k]
        if letra != ' ':
            frase_tras_frente += letra
    
    # Vendo se é Pangrama
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
    for c in frase:
        if c in alfabeto:
            alfabeto.pop(alfabeto.index(c))
    # Vendo se é epizeuxe
    lista_palavras = frase.split()
    for l in lista_palavras:
        contador = lista_palavras.count(l)
        if contador >= 2:
            break
    
    # Determinando o tipo
    if frase_tras_frente == frase_sem_espacos:
        print(f'Freddy, "{frase}" é um palíndromo!')
    elif len(alfabeto) == 0:
        print(f'Tenho certeza de que "{frase}" é um pangrama!')
    elif contador >= 2:
        print(f'Freddy, Freddy, "{frase}" é definitivamente uma epizeuxe!')
    else:
        print('Essa aqui é uma pegadinha, não há nada aqui!')

numero = int(input())
for c in range(numero):
    conteudo = input()
    tipo_frase(conteudo)


    
