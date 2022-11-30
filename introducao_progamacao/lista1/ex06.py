# Qual filme?

filme_1 = input('')
nome_1, nota_1, duracao_1 = filme_1.split("-")
nota_1 = float(nota_1)
duracao_1 = float(duracao_1)

nota_maxima = nota_1
nome_maximo = nome_1
duracao_maxima = duracao_1

filme_2 = input('')
nome_2, nota_2, duracao_2 = filme_2.split("-")
nota_2 = float(nota_2)
duracao_2 = float(duracao_2)

if nota_2 > nota_maxima:
    nome_maximo = nome_2
    nota_maxima = nota_2
    duracao_maxima = duracao_2

if nota_2 == nota_maxima:
    if duracao_2 < duracao_maxima:
        nome_maximo = nome_2
        nota_maxima = nota_2
        duracao_maxima = duracao_2

filme_3 = input('')
nome_3, nota_3, duracao_3 = filme_3.split("-")
nota_3 = float(nota_3)
duracao_3 = float(duracao_3)

if nota_3 > nota_maxima:
    nome_maximo = nome_3
    nota_maxima = nota_3
    duracao_maxima = duracao_3

if nota_3 == nota_maxima:
    if duracao_3 < duracao_maxima:
        nome_maximo = nome_3
        nota_maxima = nota_3
        duracao_maxima = duracao_3

if nota_maxima >= 4:
    print(nome_maximo)
else:
    print('Nota minima nao atingida')

