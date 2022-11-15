meninos = []
meninas = []
numero = int(input())
# completando a lista dos nomes dos meninos e meninas
for c in range(numero):
    pessoa = input()
    if pessoa[-1] == 'M':
        meninos.append(pessoa.split()[0])
    else:
        meninas.append(pessoa.split()[0])

# print das mensagens caso tenham sido digitados apenas meninas
if len(meninos) == 0:
    for c in meninas:
        if c == meninas[-1]:
            print(f'{c}, Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
        else:
            print(f'{c}, ', end='')
    print('Nao tem meninos na lista, nao precisa fazer cafe, Neuma')

# print das mensagens caso tenham sido digitados apenas meninos
elif len(meninas) == 0:
    for c in meninos:
        if c == meninos[-1]:
            print(f'{c}, Querem cafe?')
        else:
            print(f'{c}, ', end='')
    print(f'Serao necessarias {len(meninos)} porcoes de cafe')

# print das mensagens caso tenham sido digitados meninos e meninas
else:
    for c in meninos:
        if c == meninos[-1]:
            print(f'{c}, Querem cafe?')
        else:
            print(f'{c}, ', end='')
    for c in meninas:
        if c == meninas[-1]:
            print(f'{c}, Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
        else:
            print(f'{c}, ', end='')
    print(f'Serao necessarias {len(meninos)} porcoes de cafe')