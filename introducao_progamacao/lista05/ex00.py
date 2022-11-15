def pista(nome):
    if nome == 'Mario Kart Stadium':
        add = 3
    elif nome == 'Bowsers Castle':
        add = 4
    elif nome == 'Moo Moo Meadows':
        add = 5
    elif nome == 'Yoshi Valley':
        add = 6
    elif nome == 'Rainbow Road':
        add = 7
    return add

def velocidade_final(numero, adicionar):
    if numero == 0:
        return 0
    
    return adicionar + (velocidade_final(numero - 1, adicionar))


nome = input()
velocidade_inicial = int(input())
nome_pista =  input()
moedas = int(input())
moedas_ganhas = pista(nome_pista)
velocidade_ganha = velocidade_final(moedas, moedas_ganhas)
velocidade_final = velocidade_inicial + velocidade_ganha
print(f'Correndo na pista {nome_pista}, {nome} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {velocidade_final} km/h.')