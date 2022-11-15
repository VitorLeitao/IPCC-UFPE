# Dicionarios dos premios
premios = {

    'bichinho de pelucia': {
        'quantidade' : 10,
        'preco': 750,
        'resgatados': 0
    },

    'boneco articulado com armadura': {
        'quantidade': 20, 
        'preco': 1000,
        'resgatados': 0
    },

    'estatua de cena memoravel':{
        'quantidade': 10, 
        'preco': 1250,
        'resgatados': 0
    },

    'camiseta tematica':{
        'quantidade': 10, 
        'preco': 500,
        'resgatados': 0
    },

    'chaveiro': {
        'quantidade': 50, 
        'preco': 250,
        'resgatados': 0
    },

    'bolinhas': {
        'quantidade': 10000, 
        'preco': 1000,
        'resgatados': 0,
        'vendas' : 0
    },

    'resgates' : 0,
    'recebidas': 0,
    'vendidos':0
}

while True:
    comando = input()
    if comando == 'hora de fechar':
        break
    # Caso o comando seja comprar
    elif comando == 'comprar':
        quantidade = int(input())
        # Caso a compra seja valida
        if premios['bolinhas']['quantidade'] >= quantidade:
            print(f'O jogador comprou {quantidade} bolinhas por {quantidade*1000} ienes.')
            premios['bolinhas']['quantidade'] -= quantidade
            premios['bolinhas']['resgatados'] += quantidade
            premios['bolinhas']['vendas'] += 1
            premios['vendidos'] += quantidade
        else:
            print('Nao ha mais bolinhas disponiveis, melhor esperar um pouco.')
    # Caso o comando seja trocar
    elif comando == 'trocar':
        info = input()
        produto = info.split(' -')[0]
        oferecido = int(info.split('-')[-1])
        if produto in premios:
            # Caso ele tenha dinheiro e tenha produto no estoque
            if (premios[produto]['quantidade'] > 0) and (premios[produto]['preco'] <= oferecido):
                preco = premios[produto]['preco']
                print(f'O jogador trocou {preco} bolinhas por um {produto}.')
                premios[produto]['quantidade'] -= 1
                premios[produto]['resgatados'] += 1
                premios['resgates'] += 1
                premios['bolinhas']['quantidade'] += premios[produto]['preco']
                premios['recebidas'] += premios[produto]['preco']
            # Caso ele nao tenha dinheiro mas esteja no estoque
            elif (premios[produto]['quantidade'] > 0) and (premios[produto]['preco'] > oferecido):
                preco = premios[produto]['preco']
                faltando = preco - oferecido
                print(f'O jogador precisa de mais {faltando} bolinhas para trocar por um {produto}.')
            elif (premios[produto]['quantidade'] == 0):
                print(f'O jogador veio trocar suas bolinhas mas o premio {produto} nao esta disponivel.')
        else:
            print(f'O jogador veio trocar suas bolinhas mas o premio {produto} nao esta disponivel.')
        
# Printando o resultado
print()
print('O resumo do dia foi:')
quantidade_vendas = premios['bolinhas']['vendas']
quantidade_dinheiro = premios['vendidos']
print(f'Arrecadado: {quantidade_dinheiro * 1000} ienes em {quantidade_vendas} vendas;')
print('Bolinhas: {} restantes;'.format(premios['bolinhas']['quantidade']))
print('Resgates feitos: {};'.format(premios['resgates']))
print('Bolinhas recebidas: {};'.format(premios['recebidas']))

# Somatorio dos premios restantes
total_sobras = premios['bichinho de pelucia']['quantidade'] + premios['boneco articulado com armadura']['quantidade'] + premios['estatua de cena memoravel']['quantidade'] + premios['camiseta tematica']['quantidade'] + premios['chaveiro']['quantidade']
print(f'Premios: {total_sobras} restantes;')
print('Deu a hora, amanha tem mais!')