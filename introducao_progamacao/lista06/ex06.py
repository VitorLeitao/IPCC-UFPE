#Dicionario signos
dict_signos = {
    '01': {
        'signo': 'Capricórnio',
        'tipo': 'Terra'
    },
    '02': {
        'signo': 'Aquário',
        'tipo': 'Ar'
    },
    '03': {
        'signo': 'Peixes',
        'tipo': 'Terra'
    },
    '04': {
        'signo': 'Áries',
        'tipo': 'Fogo'
    },
    '05': {
        'signo': 'Touro',
        'tipo': 'Terra'
    },
    '06': {
        'signo': 'Gêmeos',
        'tipo': 'Ar'
    },

    '07': {
        'signo': 'Câncer',
        'tipo': 'Água'
    },
    '08': {
        'signo': 'Leão',
        'tipo': 'Fogo'
    },
    '09': {
        'signo': 'Virgem',
        'tipo': 'Terra'
    },
    '10': {
        'signo': 'Libra',
        'tipo': 'Ar'
    },
    '11': {
        'signo': 'Escorpião',
        'tipo': 'Água'
    },
    '12': {
            'signo': 'Sagitário',
            'tipo': 'Fogo'
        },
}

print('Digite seu nome e o nome do/da Crush:')
nome_1 = input()
nome_2 = input()
nome_1 = list(nome_1)
nome_2 = list(nome_2)
ship = []
total = 0
letras_iguais = False
# Vendo o nome do ship
for c in range(len(nome_1)):
    if nome_1[c] in nome_2:
        total += 20
        letras_iguais = True
        for i in nome_1:
            if i == nome_1[c]:
                break
            else:
                ship.append(i)
        num = nome_2.index(nome_1[c])
        for v in range(num, len(nome_2)):
            ship.append(nome_2[v])
        break
if letras_iguais == False:
    metade_1 = len(nome_1) // 2
    metade_2 = len(nome_2) // 2
    for c in range(len(nome_1)):
        if c == metade_1:
            break
        else:
            ship.append(nome_1 [c])
    for c in range(metade_2, len(nome_2)):
        ship.append(nome_2[c])
# transformando lista em str
ship_str = ''
for c in ship:
    ship_str += c

ordem_chaves = []
# Lendo as entradas do primeiro maluco
dict_1 = {}
while True:
    entrada = input()
    if entrada == '---':
        break
    ordem_chaves.append(entrada.split()[0])
    info = []
    for c in range(1, len(list(entrada.split()))):
        info.append(entrada.split()[c])
    dict_1[entrada.split()[0]] = info
# Lendo as entradas do segundo maluco
dict_2 = {}
for c in range(len(dict_1)):
    entrada = input()
    info = []
    for c in range(1, len(list(entrada.split()))):
        info.append(entrada.split()[c])
    dict_2[entrada.split()[0]] = info
###################################################################################
for g in ordem_chaves:
    # Caso a entrada seja azeitona
    if g == 'Azeitona':
        if dict_1['Azeitona'] != dict_2['Azeitona']:
            total += 50
    # Caso series
    elif g == 'Series':
        contador = 0
        for c in range(len(dict_1['Series'])):
            if dict_1['Series'][c] in dict_2['Series']:
                contador += 1
        total += (contador * 2)
    # Caso filmes
    elif g == 'Filmes':
        contador = 0
        for c in range(len(dict_1['Filmes'])):
            if dict_1['Filmes'][c] in dict_2['Filmes']:
                contador += 1
        total += (contador * 2)
    # Caso musicas
    elif g == 'Musicas':
        contador = 0
        for c in range(len(dict_1['Musicas'])):
            if dict_1['Musicas'][c] in dict_2['Musicas']:
                contador += 1
        total += (contador * 2)
    # Caso livros
    elif g == 'Livros':
        contador = 0
        for c in range(len(dict_1['Livros'])):
            if dict_1['Livros'][c] in dict_2['Livros']:
                contador += 1
        total += (contador * 2)
    # Caso aniver
    elif g == 'Aniversario':
        # Signo do primeiro cara
        index = dict_1['Aniversario'][0][3:5]
        signo_1 = dict_signos[index]['signo']
        tipo_1 = dict_signos[index]['tipo']
        # Signo e tipo do segundo cara
        index_2 = dict_2['Aniversario'][0][3:5]
        signo_2 = dict_signos[index_2]['signo']
        tipo_2 = dict_signos[index_2]['tipo']

        if signo_1 == signo_2:
            total += 10
        elif ((tipo_1 == 'Ar') and (tipo_2 == 'Água')) or ((tipo_2 == 'Ar') and (tipo_1 == 'Água')):
            total += 5
        elif ((tipo_1 == 'Fogo') and (tipo_2 == 'Terra')) or ((tipo_2 == 'Fogo') and (tipo_1 == 'Terra')):
            total += 5
    else:
        if dict_1[g] == dict_2[g]:
            total += 3
    

# Output
print(f'Hmmm, estou sentindo a conexão entre vocês... {ship_str} é um bom ship!')
print(f'Vocês combinam {total}%!')

