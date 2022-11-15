num = int(input())
lista_nomes = []
if 2 <= num <= 10:
    # Dicionario das casas
    dict_casas = {}
    for c in range(num):
        armadilha = input()
        dict_casas[c] = armadilha
    
    # Dicionario de nomes
    dict_nomes = {}
    for c in range(3):
        nome = input()
        apelido = input()
        lista_nomes.append(nome)
        lista_nomes.append(apelido)
        dict_nomes[c] = {'nome': nome,
                            'apelido': apelido
                            }
    tupla = tuple(lista_nomes)
    # Jogo em si
    for c in range(num):
        for i in range(len(dict_nomes)):
            escolha = input()
            if escolha == dict_casas[c]: # Caso a escolha seja igual a armadilha
                if len(dict_nomes) > 1:
                    print('{} caiu de uma altura de 30 metros e morreu! :O'.format(dict_nomes[i]['nome']))
                del dict_nomes[i]
            else: # Caso ele acerte a casa
                if c == (num-1):
                    print('{}, mais conhecido como {}, ganhou o jogo! Parabéns!'.format(dict_nomes[i]['nome'], dict_nomes[i]['apelido']))
                    break
                else:
                    print('{} pulou uma casa!'.format(dict_nomes[i]['nome']))
        if len(dict_nomes) == 0:
            print('Todos os jogadores morreram!')
            break
else:
    print('Faixa não permitida')