numero = int(input())
curtidas = []  #curtidas em ordem digitada(usei isso so pra armazenas a ordem na qual os nomes foram digitados)
curtidas_ordenadas = []
usuarios = []
#completando as listas
for c in range(numero):
    nome = input()
    num_curtidas = int(input())
    
    for i in range(len(curtidas_ordenadas)):
        if num_curtidas < curtidas_ordenadas[i]:
            curtidas_ordenadas.insert(i, num_curtidas)
            break
    else:
        curtidas_ordenadas.append(num_curtidas)

    usuarios.append(nome)
    curtidas.append(num_curtidas)

# achando o nome da pessoa com mais curtidas
posicao_maximo = curtidas.index(max(curtidas))
nome_maximo = usuarios[posicao_maximo]



# printando a lista em ordem inversa
print('O numero de curtidas dos videos que vao aparecer na For You segue a ordem:')
for c in range((len(curtidas_ordenadas)-1),-1,-1):

    if c == 0:
        print(f'{curtidas_ordenadas[c]}')
    else:
        print(f'{curtidas_ordenadas[c]}, ',end='')
print(f'O primeiro usuario que vai aparecer na For You e {nome_maximo}!')