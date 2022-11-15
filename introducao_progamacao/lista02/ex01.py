qt_competidores = int(input(''))
for c in range(0, qt_competidores):
    nome = input('')
    pontuacao = int(input(''))
    if c == 0:
        nome_maximo = nome
        pontuacao_maxima = pontuacao
    else:
        if pontuacao > pontuacao_maxima:
            nome_maximo = nome
            pontuacao_maxima = pontuacao

print(f'{nome_maximo} e o novo anjo!')
