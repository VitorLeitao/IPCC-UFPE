lista = []
while True:
    comando = input()
    if comando == 'lista finalizada':
        print('A lista ficou da seguinte forma:')
        for c in lista:
            if c == lista[-1]:
                print(c)
            else:
                print(f'{c} ',end='')
        break
    
    # caso o comando seja adicionar
    elif comando == 'adicionar':
        nome_posicao = input()
        nome = nome_posicao.split()[0]
        posicao = nome_posicao.split()[-1]
        posicao = int(posicao)
        lista.insert(posicao, nome)
    
    # caso o comando seja remover
    elif comando == 'remover':
        nome = input()
        lista.remove(nome)
    
    # Caso o comando seja atualizar indice
    elif comando == 'atualizar indice':
        nome_posicao = input()
        nome = nome_posicao.split()[0]
        posicao = nome_posicao.split()[-1]
        posicao = int(posicao)
        # verificando se a posição é igual a antiga
        if posicao == lista.index(nome):
            print('Nada mudou, a lista permanece igual')
        else:
            lista.remove(nome)
            lista.insert(posicao, nome)
    
    # Caso o comando seja imprimir a lista
    elif comando == 'imprimir lista atual':
        for c in lista:
            if c == lista[-1]:
                print(c)
            else:
                print(f'{c} ',end='')
    
    # Se o comando for invalido
    else:
        print('Opçao não encontrada')
    
