quantidade = int(input())
curtidas = []
for c in range(quantidade):
    frase = input()
    numerico = frase.split('-')[-1]
    numerico = int(numerico)
    numero_string = frase.split('-')[0]

    for i in range(len(curtidas)):
        valor_numerico = curtidas[i].split('-')[-1]
        valor_numerico = int(valor_numerico)
        valor_string = curtidas[i].split('-'[0])

        if numerico < valor_numerico:
            curtidas.insert(i, frase)
            break
        if numerico == valor_numerico:
            if len(frase.split('-')[0]) < len(valor_string):
                curtidas.insert(i, frase)
                break
    else:
        curtidas.append(frase)

for c in curtidas:
    print(c)