numero = int(input())
lista_total = []
lista_uti = []
lista_life = []
lista_dan = []
# Preenchendo as listas
for c in range(numero):
    frase = input()
    lista_total.append(frase)
    if frase.split(', ')[-1] == 'Utilidades':
        lista_uti.append(frase)
    elif frase.split(', ')[-1] == 'Lifestyle':
        lista_life.append(frase)
    elif frase.split(', ')[-1] == 'Dancinhas':
        lista_dan.append(frase)

# ==========INFORMAÇÕES DANCINHAS=========
if len(lista_dan) > 0:
    tamanho_dan = len(lista_dan)
# MEDIA SEGUIMORES
    soma_dan = 0
    for c in lista_dan:
        valor = float(c.split(', ')[1][0:-1])
        if c.split(', ')[1][-1] == 'K':
            valor = valor / 1000
        soma_dan += valor
    media_dan = soma_dan / tamanho_dan
# MAXIMO VISUALIZAÇÃO
    for c in lista_dan:
        valor = float(c.split(', ')[2][0:-1])
        if c.split(', ')[2][-1] == 'K':
            valor = valor / 1000
        if c == lista_dan[0]:
            maximo_dan = valor
        else:
            if valor > maximo_dan:
                maximo_dan = valor
# ==========INFORMAÇÕES UTILIDADES=========
if len(lista_uti) > 0:
    tamanho_uti = len(lista_uti)
# MEDIA SEGUIMORES
    soma_uti = 0
    for c in lista_uti:
        valor = float(c.split(', ')[1][0:-1])
        if c.split(', ')[1][-1] == 'K':
            valor = valor / 1000
        soma_uti += valor
    media_uti = soma_uti / tamanho_uti
# MAXIMO VISUALIZAÇÃO
    for c in lista_uti:
        valor = float(c.split(', ')[2][0:-1])
        if c.split(', ')[2][-1] == 'K':
            valor = valor / 1000
        if c == lista_uti[0]:
            maximo_uti = valor
        else:
            if valor > maximo_uti:
                maximo_uti = valor
# ==========INFORMAÇÕES LIFESTYLE=========
if len(lista_life) > 0:
    tamanho_life = len(lista_life)
# MEDIA SEGUIMORES
    soma_life = 0
    for c in lista_life:
        valor = float(c.split(', ')[1][0:-1])
        if c.split(', ')[1][-1] == 'K':
            valor = valor / 1000
        soma_life += valor
    media_life = soma_life / tamanho_life
# MAXIMO VISUALIZAÇÃO
    for c in lista_life:
        valor = float(c.split(', ')[2][0:-1])
        if c.split(', ')[2][-1] == 'K':
            valor = valor / 1000
        if c == lista_life[0]:
            maximo_life = valor
        else:
            if valor > maximo_life:
                maximo_life = valor
# imprimindo os resultados de lifestyle
print('Lifestyle;')
if len(lista_life) > 0:
    media_life = str(media_life)[0:(str(media_life).index(".")) + 2]
    maximo_life = str(maximo_life)[0:(str(maximo_life).index(".")) + 3]
    print(f'Quantidade de Tiktokers: {tamanho_life}')
    print(f'Media de seguidores: {float(media_life):.1f}M')
    print(f'Maximo de visualizações: {float(maximo_life):.2f}M')
else:
    print('Nao foram informados dados sobre esta categoria.')
print()

# imprimindo os resultador de utilidades
print('Utilidades;')
if len(lista_uti) > 0:
    media_uti = str(media_uti)[0:(str(media_uti).index(".")) + 2]
    maximo_uti = str(maximo_uti)[0:(str(maximo_uti).index(".")) + 3]
    print(f'Quantidade de Tiktokers: {tamanho_uti}')
    print(f'Media de seguidores: {float(media_uti):.1f}M')
    print(f'Maximo de visualizações: {float(maximo_uti):.2f}M')
else:
    print('Nao foram informados dados sobre esta categoria.')
print()

# imprimindo os resultador de dancinhas
print('Dancinhas;')
if len(lista_dan) > 0:
    media_dan = str(media_dan)[0:(str(media_dan).index(".")) + 2]
    maximo_dan = str(maximo_dan)[0:(str(maximo_dan).index(".")) + 3]
    print(f'Quantidade de Tiktokers: {tamanho_dan}')
    print(f'Media de seguidores: {float(media_dan):.1f}M')
    print(f'Maximo de visualizações: {float(maximo_dan):.2f}M')
else:
    print('Nao foram informados dados sobre esta categoria.')
print()
# Fazendo a mensagem final
for c in lista_total:
    valor = float(c.split(', ')[1][0:-1])
    nome = c.split(', ')[0]
    categoria = c.split(', ')[-1]
    if c.split(', ')[1][-1] == 'K':
            valor = valor / 1000
    if c == lista_total[0]:
        valor_maximo = valor
        nome_maximo = nome
        categoria_maximo = c.split(', ')[-1]
    else:
        if valor > valor_maximo:
            valor_maximo = valor
            nome_maximo = nome
            categoria_maximo = c.split(', ')[-1]
print(f'Os olhares do mundo estao sobre {nome_maximo.upper()}, que conta com {valor_maximo}M de seguidores vendo seus videos diarios de {categoria_maximo}!')
