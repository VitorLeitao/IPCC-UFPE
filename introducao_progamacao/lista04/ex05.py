nomes = ['Sam', 'Chris', 'Ashley', 'Jessica', 'Mike', 'Emily', 'Matt']
lista_status = ['vivo', 'vivo', 'vivo', 'vivo', 'vivo', 'vivo', 'vivo']
def achar_indice(nome):
    if nome == 'Sam':
        index = 0
    elif nome == 'Chris':
        index = 1
    elif nome == 'Ashley':
        index = 2
    elif nome == 'Jessica':
        index = 3
    elif nome == 'Mike':
        index = 4
    elif nome == 'Emily':
        index = 5
    elif nome == 'Matt':
        index = 6
    return index
def mudar_matriz(index_1, index_2, string):
    if string == 'X':
        matriz[index_1][index_2] -= 1
        matriz[index_2][index_1] -= 1
    else:
        matriz[index_1][index_2] += 1
        matriz[index_2][index_1] += 1
def parte_dinamica(string):
    if len(string.split()) >= 2:
        primeiro_nome = string.split()[0]
        segundo_nome = string.split()[-1]
        primeiro_index = achar_indice(primeiro_nome)
        segundo_index = achar_indice(segundo_nome)
        if (lista_status[primeiro_index] == 'vivo') and (lista_status[segundo_index] == 'vivo'):
            if matriz[primeiro_index][segundo_index] > 6:
                print(f'felizmente {segundo_nome} ajudou {primeiro_nome} a escapar do Wendigo.')
            else:
                print(f'que pena! {segundo_nome} nao conseguiu ajudar {primeiro_nome} do ataque do Wendigo.')
                lista_status[primeiro_index] = 'morto'
        else:
            print('entrada invalida!!! voce so pode jogar com jogadores vivos')
    else:
        index = achar_indice(string)
        if lista_status[index] == 'vivo':
            soma = 0
            contador = 0
            for c in range(len(matriz[index])):
                if (matriz[index][c] != -1) and (lista_status[c] != 'morto'):
                    soma += matriz[index][c]
                    contador += 1
            if contador > 0:
                media = (soma / contador)
            else:
                media = 0
            if media > 5:
                print(f'UFA!!! foi por pouco mas {string} conseguiu escapar do Wendigo.')
            else:
                print(f'{string} infelizmente nao conseguiu sobreviver ao ataque do Wendigo.')
                lista_status[index] = 'morto'

        else:
            print(f'entrada invalida!!! voce so pode jogar com jogadores vivos')

matriz = [
    [-1, 5, 5, 5, 5, 5, 5],
    [5, -1, 6, 5, 5, 5, 5],
    [5, 6, -1, 5, 5, 5, 5],
    [5, 5, 5, -1, 7, 4, 5],
    [5, 5, 5, 7, -1, 3, 4],
    [5, 5, 5, 4, 3, -1, 7],
    [5, 5, 5, 5, 4, 7, -1]
]

num_1 = int(input())
for c in range(num_1):
    string = input()
    nome_1 = string.split()[0]
    nome_2 = string.split()[-1]
    interacao = string.split()[1]
    index_nome_1 = achar_indice(nome_1)
    index_nome_2 = achar_indice(nome_2)
    mudar_matriz(index_nome_1, index_nome_2, interacao)

num_2 = int(input())
for c in range(num_2):
    string_entrada = input()
    parte_dinamica(string_entrada)
print()

if 'vivo' in lista_status:
    print('Sobreviventes:')
    for c in range(len(lista_status)):
        if lista_status[c] == 'vivo':
            print(nomes[c])
else:
    print('Tristemente, ninguém sobreviveu')
