'''numero = int(input())
if 1 <= numero <= 6:
    if numero % 2 == 0:
        if numero == 2:
            arma = 'Garrafa de Whisky'
        if numero == 4:
            arma = 'Lamina Escondida'
        if numero == 6:
            arma = 'Canivete'
        print(f'A arma corpo a corpo escolhida foi: {arma}\nA arma corpo a corpo escolhida e cortante')
    else:
        if numero == 1:
            arma = 'Cassetete'
        if numero == 3:
            arma = 'Soco Ingles'
        if numero == 5:
            arma = 'Pe de Cabra'
        print(f'A arma corpo a corpo escolhida foi: {arma}\nA arma corpo a corpo escolhida e atordoante')
else:
    print('Numero invalido')'''

numero = int(input())
if 1 <= numero <= 6:
    if numero % 2 == 0:
        tipo_arma = 'cortante'
    else:
        tipo_arma = 'atordoante'

    if numero == 1:
        arma = 'Cassetete'
    if numero == 2:
        arma = 'Garrafa de Whisky'
    if numero == 3:
        arma = 'Soco Ingles'
    if numero == 4:
        arma = 'Lamina Escondida'
    if numero == 5:
        arma = 'Pe de Cabra'
    if numero == 6:
        arma = 'Canivete'

    print(f'A arma corpo a corpo escolhida foi: {arma}\nA arma corpo a corpo escolhida e {tipo_arma}')
else:
    print('Numero invalido')