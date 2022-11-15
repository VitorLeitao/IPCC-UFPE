letra = input()
quantidade_jogadores = int(input())
for c in range(0, quantidade_jogadores):
    nome, palavra = input().split('-')
    qtd_acertos = 0

    for i in palavra:
        if i == letra:
            qtd_acertos += 1
    if c == 0:
        nome_vencedor = nome
        palavra_vencedor = palavra
        qtd_vencedor = qtd_acertos
    else:
        if qtd_acertos > qtd_vencedor:
            nome_vencedor = nome
            palavra_vencedor = palavra
            qtd_vencedor = qtd_acertos
if nome_vencedor == 'Prior':
    print(f'Joga y joga! Mago Prior e o novo lider com a palavra {palavra_vencedor} com {qtd_vencedor} aparicoes da letra {letra}.')
else:
    print(f'Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {nome_vencedor}, com a palavra {palavra_vencedor} e {qtd_vencedor} aparicoes da letra {letra}.')
