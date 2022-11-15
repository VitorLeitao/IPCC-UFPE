lista_nomes = []
lista_curtidas = []
lista_ordenada = []
# preenchendo as listas
for c in range(3):
    nome = input()
    quant_1 = int(input())
    quant_2 = int(input())
    quant_media = (quant_1 + quant_2) / 2
    lista_nomes.append(nome)
    lista_curtidas.append(quant_media)
    for c in range(len(lista_ordenada)):
        if quant_media > lista_ordenada[c]:
            lista_ordenada.insert(c, quant_media)
            break
    else:
        lista_ordenada.append(quant_media)

# printando as colocaçoes
contador = 1
for c in range(0, len(lista_ordenada)): # varrendo os valores
    posicao_atual = lista_curtidas.index(lista_ordenada[c]) # vaiachar a posição do valor atual da lista ordenada em lista_curtidas
    nome_atual = lista_nomes[posicao_atual]
    valor_atual = lista_ordenada[c]

    print(f'{contador}º Lugar: {nome_atual} com a media de views: {int(valor_atual)}')
    contador += 1


