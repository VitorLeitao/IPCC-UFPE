# Torneio dos Dunphy

'''alfabeto = 'abcdefghijklmnopqrstuvwxyz'

nome_1 = input()
pontos_1 = int(input())
nome_maximo = nome_1
pontos_maximos = pontos_1

nome_2 = input()
pontos_2 = int(input())
if pontos_2 > pontos_maximos:
    pontos_medio = pontos_maximos
    nome_medio = nome_maximo
    pontos_maximos = pontos_2
    nome_maximo = nome_2
elif pontos_2 == pontos_maximos:
    if alfabeto.find(nome_2[0].lower()) >= alfabeto.find(nome_maximo[0].lower()):
        pontos_medio = pontos_maximos
        nome_medio = nome_maximo
        pontos_maximos = pontos_2
        nome_maximo = nome_2
    else:
        pontos_medio = pontos_2
        nome_medio = nome_2
else:
    pontos_medio = pontos_2
    nome_medio = nome_2

nome_3 = input()
pontos_3 = int(input())
if pontos_3 > pontos_maximos:
    pontos_minimo = pontos_medio
    nome_minimo = nome_medio
    pontos_medio = pontos_maximos
    nome_medio = nome_maximo
    pontos_maximos = pontos_3
    nome_maximo = nome_3
elif pontos_3 == pontos_maximos:
    if alfabeto.find(nome_3[0].lower()) >= alfabeto.find(nome_maximo[0].lower()):
        pontos_minimo = pontos_medio
        nome_minimo = nome_medio
        pontos_medio = pontos_maximos
        nome_medio = nome_maximo
        pontos_maximos = pontos_3
        nome_maximo = nome_3
    else:
        if pontos_3 > pontos_medio:
            pontos_minimo = pontos_medio
            nome_minimo = nome_medio
            pontos_medio = pontos_3
            nome_medio = nome_3
        elif pontos_3 == pontos_medio:
            if alfabeto.find(nome_3[0].lower()) >= alfabeto.find(nome_medio[0].lower()):
                pontos_minimo = pontos_medio
                nome_minimo = nome_medio
                pontos_medio = pontos_3
                nome_medio = nome_3
            else:
                pontos_minimo = pontos_3
                nome_minimo = nome_3
        else:
            pontos_minimo = pontos_3
            nome_minimo = nome_3
else:
    if pontos_3 > pontos_medio:
        pontos_minimo = pontos_medio
        nome_minimo = nome_medio
        pontos_medio = pontos_3
        nome_medio = nome_3
    elif pontos_3 == pontos_medio:
        if alfabeto.find(nome_3[0].lower()) >= alfabeto.find(nome_medio[0].lower()):
            pontos_minimo = pontos_medio
            nome_minimo = nome_medio
            pontos_medio = pontos_3
            nome_medio = nome_3
        else:
            pontos_minimo = pontos_3
            nome_minimo = nome_3
    else:
        pontos_minimo = pontos_3
        nome_minimo = nome_3

print(nome_minimo, pontos_minimo)
print(nome_medio, pontos_medio)
print(nome_maximo, pontos_maximos)'''


# Torneio dos Dunphy


nome_1 = input()
pontos_1 = int(input())
nome_maximo = nome_1
pontos_maximos = pontos_1

nome_2 = input()
pontos_2 = int(input())
if pontos_2 > pontos_maximos:
    pontos_medio = pontos_maximos
    nome_medio = nome_maximo
    pontos_maximos = pontos_2
    nome_maximo = nome_2
elif pontos_2 == pontos_maximos:
    if nome_2 >= nome_maximo:
        pontos_medio = pontos_maximos
        nome_medio = nome_maximo
        pontos_maximos = pontos_2
        nome_maximo = nome_2
    else:
        pontos_medio = pontos_2
        nome_medio = nome_2
else:
    pontos_medio = pontos_2
    nome_medio = nome_2

nome_3 = input()
pontos_3 = int(input())
if pontos_3 > pontos_maximos:
    pontos_minimo = pontos_medio
    nome_minimo = nome_medio
    pontos_medio = pontos_maximos
    nome_medio = nome_maximo
    pontos_maximos = pontos_3
    nome_maximo = nome_3
elif pontos_3 == pontos_maximos:
    if nome_3 >= nome_maximo:
        pontos_minimo = pontos_medio
        nome_minimo = nome_medio
        pontos_medio = pontos_maximos
        nome_medio = nome_maximo
        pontos_maximos = pontos_3
        nome_maximo = nome_3
    else:
        if pontos_3 > pontos_medio:
            pontos_minimo = pontos_medio
            nome_minimo = nome_medio
            pontos_medio = pontos_3
            nome_medio = nome_3
        elif pontos_3 == pontos_medio:
            if nome_3 >= nome_medio:
                pontos_minimo = pontos_medio
                nome_minimo = nome_medio
                pontos_medio = pontos_3
                nome_medio = nome_3
            else:
                pontos_minimo = pontos_3
                nome_minimo = nome_3
        else:
            pontos_minimo = pontos_3
            nome_minimo = nome_3
else:
    if pontos_3 > pontos_medio:
        pontos_minimo = pontos_medio
        nome_minimo = nome_medio
        pontos_medio = pontos_3
        nome_medio = nome_3
    elif pontos_3 == pontos_medio:
        if nome_3 >= nome_medio:
            pontos_minimo = pontos_medio
            nome_minimo = nome_medio
            pontos_medio = pontos_3
            nome_medio = nome_3
        else:
            pontos_minimo = pontos_3
            nome_minimo = nome_3
    else:
        pontos_minimo = pontos_3
        nome_minimo = nome_3

print(nome_minimo, pontos_minimo)
print(nome_medio, pontos_medio)
print(nome_maximo, pontos_maximos)