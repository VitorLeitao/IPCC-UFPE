numero = int(input())
utilidades = []
dancinhas = []
lifestyle = []
lista_total = []
for c in range(numero):
    frase = input()
    # preenchendo as listas
    if frase.split(', ')[-1] == 'Utilidades':
        utilidades.append(frase)
    elif frase.split(', ')[-1] == 'Lifestyle':
        lifestyle.append(frase)
    elif frase.split(', ')[-1] == 'Dancinhas':
        dancinhas.append(frase)
    lista_total.append(frase)


# ==============Informações sobre lifestyle===============
if len(lifestyle) > 0:
    quantidade_lifestyle = len(lifestyle)
    # Media de seguidores
    soma = 0
    for c in lifestyle:
        valores = c.split(', ')
        valor = valores[1][0:-1]
        valor = float(valor)
        if valores[1][-1] == 'K':
            valor = valor / 1000
        soma += valor
    media_lifestyle = soma / len(lifestyle)
    # Colocando M ou K no final da media

    media_lifestyle = media_lifestyle / 1000000
    media_lifestyle_final = f'{media_lifestyle:.1f}M'
    # Maximo seguidores
    for c in range(0, len(lifestyle)):
        valores = lifestyle[c].split(', ')
        nome = valores[0]
        valor = valores[2][0:-1]
        valor = float(valor)
        if valores[1][-1] == 'K':
            valor = valor / 1000
        if c == 0:
            valor_maximo_lifestyle = valor
            nome_maximo_lifestyle = nome
        else:
            if valor > valor_maximo_lifestyle:
                valor_maximo_lifestyle = valor
                nome_maximo_lifestyle = nome
    # Colocando M ou K no final do valor maximo
    
    valor_maximo = valor_maximo_lifestyle
    valor_maximo_final = f'{valor_maximo:.2f}M'

# ===============Informações sobre utilidades===================
if len(utilidades) > 0:
    quantidades_utilidades = len(utilidades)
    # Media de seguidores
    soma = 0
    for c in utilidades:
        valores = c.split(', ')
        valor = valores[1][0:-1]
        valor = float(valor)
        if valores[1][-1] == 'K':
            valor = valor / 1000
        soma += valor
    media_utilidades = soma / len(utilidades)
    # Colocando M ou K no final da media
    media_utilidades_final = f'{media_utilidades:.1f}M'
    # Maximo seguidores
    for c in range(0, len(utilidades)):
        valores = utilidades[c].split(', ')
        nome = valores[0]
        valor = valores[2][0:-1]
        valor = float(valor)
        if valores[1][-1] == 'K':
            valor = valor / 1000
        if c == 0:
            valor_maximo_utilidades = valor
            nome_maximo_utilidades = nome
        else:
            if valor > valor_maximo_utilidades:
                valor_maximo_utilidades = valor
                nome_maximo_utilidades = nome
    # Colocando M ou K no final do valor maximo

    valor_maximo = valor_maximo_utilidades
    valor_utilidades_final = f'{valor_maximo:.2f}M'

# ==================Informações sobre dancinhas====================
if len(dancinhas) > 0:
    quantidades_dancinhas = len(dancinhas)
    # Media de seguidores
    soma = 0
    for c in dancinhas:
        valores = c.split(', ')
        valor = valores[1][0:-1]
        valor = float(valor)
        if valores[1][-1] == 'K':
            valor = valor / 1000
        soma += valor
    media_dancinhas = soma / len(dancinhas)
    # Colocando M ou K no final da media
    media_dancinhas_final = f'{media_dancinhas:.1f}M'
    # Maximo seguidores
    for c in range(0, len(dancinhas)):
        valores = dancinhas[c].split(', ')
        nome = valores[0]
        valor = valores[2][0:-1]
        valor = float(valor)
        if valores[1][-1] == 'K':
            valor = valor / 1000
        if c == 0:
            valor_maximo_dancinhas = valor
            nome_maximo_dancinhas = nome
        else:
            if valor > valor_maximo_dancinhas:
                valor_maximo_dancinhas = valor
                nome_maximo_dancinhas = nome
    # Colocando M ou K no final do valor maximo

    valor_maximo = valor_maximo_dancinhas
    valor_dancinhas_final = f'{valor_maximo:.2f}M'

# imprimindo os resultados de lifestyle
if len(lifestyle) > 0:
    print('Lifestyle;')
    print(f'Quantidade de Tiktokers: {quantidade_lifestyle}')
    print(f'Media de seguidores: {media_lifestyle_final}')
    print(f'Maximo de visualizações: {valor_maximo_final}')
else:
    print('Nao foram informados dados sobre esta categoria.')
print()

# imprimindo os resultador de utilidades
if len(utilidades) > 0:
    print('Utilidades;')
    print(f'Quantidade de Tiktokers: {quantidades_utilidades}')
    print(f'Media de seguidores: {media_utilidades_final}')
    print(f'Maximo de visualizações: {valor_utilidades_final}')
else:
    print('Nao foram informados dados sobre esta categoria.')
print()

# imprimindo os resultador de dancinhas
if len(dancinhas) > 0:
    print('Dancinhas;')
    print(f'Quantidade de Tiktokers: {quantidades_dancinhas}')
    print(f'Media de seguidores: {media_dancinhas_final}')
    print(f'Maximo de visualizações: {valor_dancinhas_final}')
else:
    print('Nao foram informados dados sobre esta categoria.')
print()

# Fazendo a mensagem final
for c in lista_total:
    valor = c.split(', ')[1][0: -1]
    valor = float(valor)
    nome = c.split(', ')[0]
    if c[1][-1] == 'K':
            valor = valor / 1000

    if c == lista_total[0]:
        valor_maximo = valor
        nome_maximo = nome
    else:
        if valor > valor_maximo:
            valor_maximo = valor
            nome_maximo = nome



valor_final = f'{valor_maximo:.1f}M'

print(f'Os olhares do mundo estao sobre {nome_maximo.upper()}, que conta com {valor_final} de seguidores vendo seus videos diarios de Dancinhas!')