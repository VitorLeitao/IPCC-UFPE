numero = int(input())
lista = []
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in range(numero):
    hashtag = input('')
    contador = 0
    # Vendo se tem alguma letra maiuscula na hashtag
    for c in hashtag:
        for i in letras_maiusculas:
            if c == i:
                contador += 1
    
    # colocando a hashtag na lista apenas se for composta apenas de letras minusculas e ordenando a lista
    if contador == 0:
        for i in range(len(lista)):
            if hashtag[1] < lista[i][1]:
                lista.insert(i, hashtag)
                break
        else:
            lista.append(hashtag)

for c in lista:
    print(c)




