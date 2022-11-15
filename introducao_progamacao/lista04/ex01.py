# Funções
def espacos_vazios(slots, itens):
    slots_sobrando = (slots - itens)
    return slots_sobrando

def novo_inventario(pochetes, slots, itens):
    slots_novos = (pochetes * 2) + slots
    slotes_sobrando = int(slots_novos - itens)
    return slotes_sobrando

lista_itens = []
num_slotes = int(input())
num_itens = int(input())
espacos_sobrando_inicial = espacos_vazios(num_slotes, num_itens)

# Lendo os valores e colocando em uma lista
for c in range(num_itens):
    infos = input()
    arma = infos.split(' -')[0]
    numero = infos.split('- ')[-1]
    frase = f'{arma} [{numero}]'
    lista_itens.append(frase)
num_pochetes = int(input())
espacos_sobrando_final = novo_inventario(num_pochetes, num_slotes, num_itens)
novos_slots = (num_pochetes * 2) + num_slotes

#output
print(f'Voce possui {num_slotes} slots no inventario e {num_itens} estao ocupados.')
print(f'Espacos sobrando [{espacos_sobrando_inicial}]')
print()
if len(lista_itens) > 0:
    print('Lista de itens:')
    for c in lista_itens:
        print(c)
else:
    print('Seu inventário ainda está vazio. Que sorte... ou azar. Tome cuidado.')
print()
if num_pochetes > 0:
    print(f'Voce conseguiu {num_pochetes} pochete(s) e agora possui {novos_slots} slots de inventario.')
    print(f'Espacos sobrando [{espacos_sobrando_final}]')
else:
    print('Você ainda não encontrou pochetes. Seus espaços continuam os mesmos.')




