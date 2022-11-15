# listas iniciais
lista_liberos = []
lista_levant = []
lista_central = []
lista_pont = []
lista_oposto = []
total = []
while True:
    comando = input()
    # Caso o comando seja adicionar
    if comando == 'adicionar':
        frase = input()
        nome = frase.split(': ')[0]
        posicao = frase.split(': ')[-1]
        # Olhando em qual lista adicionar
        if posicao == 'Levantador':  # LEVANTADOR
            lista_levant.append(nome)
            if len(lista_levant) >= 5:
                print('Cuidado! voce ja possui 5 levantadores')
        elif posicao == 'Oposto': # OPOSTO
            lista_oposto.append(nome)
            if len(lista_oposto) >= 5:
                print('Cuidado! voce ja possui 5 opostos')
        elif posicao == 'Central': # CENTRAL
            lista_central.append(nome)
            if len(lista_central) >= 5:
                print('Cuidado! voce ja possui 5 centrais')
        elif posicao == 'Libero': # LIBERO
            lista_liberos.append(nome)
            if len(lista_liberos) > 2:
                print('ERRO: liberos demais, nao temos uniformes suficientes')
                break
        elif posicao == 'Ponteiro': # PONTEIRO
            lista_pont.append(nome)
            if len(lista_pont) >= 5:
                print('Cuidado! voce ja possui 5 ponteiros')

        total.append(nome)
        if len(total) > 18:
            print('ERRO: voce estrapolou o numero de jogadores')
            break
        
    # COMANDO RELATORIO
    elif comando == 'relatorio':
        print(f'No nosso time ja possuimos:\nLiberos: {len(lista_liberos)}\nLevantadores: {len(lista_levant)}\nPonteiros: {len(lista_pont)}\nCentrais: {len(lista_central)}\nOpostos: {len(lista_oposto)}\nTOTAL: {len(total)}')

    # COMANDO NOMES
    elif comando == 'nomes':
        posicao = input()
        # MODIFICANDO A SAIDA DEPENDENDO DE QUAL POSICAO É 
        if posicao == 'Levantador':  # LEVANTADORES
            if len(lista_levant) > 0:
                print('Os levantadores sao:')
                for c in lista_levant:
                    print(c)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Central':  # CENTRAIS
            if len(lista_central) > 0:
                print('Os centrais sao:')
                for c in lista_central:
                    print(c)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Libero':  # LIBEROS
            if len(lista_liberos) > 0:
                print('Os liberos sao:')
                for c in lista_liberos:
                    print(c)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Oposto':  # OPOSTOS
            if len(lista_oposto) > 0:
                print('Os opostos sao:')
                for c in lista_oposto:
                    print(c)
            else:
                print('Ainda nao temos jogadores nessa posicao')
        elif posicao == 'Ponteiro':  # PONTEIROS
            if len(lista_pont) > 0:
                print('Os ponteiros sao:')
                for c in lista_pont:
                    print(c)
            else:
                print('Ainda nao temos jogadores nessa posicao')
    #COMANDO BUSCAR
    elif comando == 'buscar':
        nome = input()
        if nome in total:
            if nome == 'Samuel':
                print('Sim, Samuel, voce ja esta na lista de jogadores')
            else:
                print(f'Sim, {nome} esta na lista de jogadores')
        else:
            if nome == 'Samuel':
                print('Como voce pode esquecer de si mesmo? Voce nao esta na lista')
            else:
                print(f'O jogador {nome} nao esta na lista de jogadores')
    # COMANDO FIM
    elif comando == 'fim':
        break
    # COMANDO INVALIDO
    else:
        print('***COMANDO INVALIDO***')

# VENDO SE O TIME ATENDE AS REGRAS
if (len(lista_central)>=2) and (len(lista_levant)>=2) and (len(lista_oposto)>=2) and (len(lista_pont)>=2) and (len(lista_liberos) == 2) and (len(total) <= 18):
    print(f'O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos nossos {len(total)} jogadores!')
else:
    print('Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :(')


