dict_cartas = {
    'As': {
        'pontos' : 1,
        'quantidade': {
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    },
    '2': {
        'pontos' : 2,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '3': {
        'pontos' : 3,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '4': {
        'pontos' : 4,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '5': {
        'pontos' : 5,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '6': {
        'pontos' : 6,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '7': {
        'pontos' : 7,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '8': {
        'pontos' : 8,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    },
    '9': {
        'pontos' : 9,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    '10': {
        'pontos' : 10,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    'Valete': {
        'pontos' : 11,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    'Dama': {
        'pontos' : 11,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }, 
    'Rei': {
        'pontos' : 11,
        'quantidade':{
            'ouros': 1,
            'paus': 1,
            'espadas': 1,
            'copas': 1
        }
    }
}

naipes = ('ouros', 'paus', 'espadas', 'copas')
# Rodada do player
pontos_player = 0
while True:
    carta = input()
    if not(carta.split()[-1] in naipes):
        print(f'A carta {carta} não existe, não me enganarão!')
    elif dict_cartas[carta.split()[0]]['quantidade'][carta.split()[-1]] == 0:
        print('EIEIEI, QUE ROUBO É ESSE!!!')
    else:
        pontuacao = dict_cartas[carta.split()[0]]['pontos']
        dict_cartas[carta.split()[0]]['quantidade'][carta.split()[-1]] -= 1
        pontos_player += pontuacao
    if pontos_player >= 17:
        break

print(f'Minha rodada acaba por aqui com {pontos_player} pontos.')
if pontos_player > 21:
    print('Ah não, passei do ponto!')
    
else:
    if (pontos_player == 21):
            print('Blackjack!')
    # Rodada da Casa
    pontos_casa = 0
    while True:
        carta = input()
        if not(carta.split()[-1] in naipes):
            print(f'A carta {carta} não existe, não me enganarão!')
        elif dict_cartas[carta.split()[0]]['quantidade'][carta.split()[-1]] == 0:
            print('EIEIEI, QUE ROUBO É ESSE!!!')
        else:
            pontuacao = dict_cartas[carta.split()[0]]['pontos']
            dict_cartas[carta.split()[0]]['quantidade'][carta.split()[-1]] -= 1
            pontos_casa += pontuacao
        if pontos_casa >= 17:
            break   
        
    print(f'A rodada da casa acaba por aqui com {pontos_casa} pontos.')
    
    if (pontos_casa == 21):
        print('Blackjack!')
    
    if pontos_casa > 21:
        print('AEEEEEEE, ele passou de 21, poder ir pagando chefa!!')
    elif pontos_player == pontos_casa:
        print('A próxima eu levo.')
    elif pontos_player > pontos_casa:
        print('O dinheiro é meu!')
    elif pontos_casa > pontos_player:
        print('Perdi tudo, F.')