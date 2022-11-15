import math
def combate(contador, vida_1, vida_2, atk_1, atk_2, spatk_1, spatk_2, def_1, def_2, nome_1, nome_2, vida_base):
    if (vida_1 <= 0) or (vida_2 <= 0):
        return vida_1, vida_2
    # Caso o round seja entre 1-5
    if contador < 5:
        if contador % 2 == 0: # Round do jogador 2
            dano = atk_2 - def_1
        else: # Round do jogador 1
            dano = atk_1 - def_2 
            
    # Round 5-n
    else:
        confirmar = fibonacci(contador - 1)
        # Caso n em fibonacci seja par
        if confirmar % 2 == 0:
            if contador % 2 == 0: # Round jogador 2
                dano = spatk_2
            else: # Round jogador 1
                dano = spatk_1
        # N impar
        else:
            if contador % 2 == 0: # Round do jogador 2
                dano = atk_2 - def_1
            else: # Round do jogador 1
                dano = atk_1 - def_2 
    # Vendo quem perde vida
    if dano >= 0:
        if contador % 2 == 0: # Jogador 2
            vida_1 -= dano
        else:
            vida_2 -= dano
    # Printando quem perde vida

    print(f'\nROUND {contador}:')
    # jogador 1
    print(f'VIDA {nome_1}:')
    cubinho = vida_base / 10
    cubinhos_restantes = math.ceil(vida_1 / cubinho)# aaa
    for c in range(1, 11):
        if c == 10:
            if c > cubinhos_restantes:
                print('-')
            else:
                print('*')
        else:
            if c > cubinhos_restantes:
                print('-', end=' ')
            else:
                print('*', end=' ')
    # jogador2
    print(f'VIDA {nome_2}:') 
    cubinho = vida_base / 10
    cubinhos_restantes = math.ceil(vida_2 / cubinho)
    for c in range(1, 11):
        if c == 10:
            if c > cubinhos_restantes:
                print('-')
            else:
                print('*')
        else:
            if c > cubinhos_restantes:
                print('-', end=' ')
            else:
                print('*', end=' ')
    return combate(contador + 1, vida_1, vida_2, atk_1, atk_2, spatk_1, spatk_2, def_1, def_2, nome_1, nome_2, vida_base)

def fibonacci(numero):                         
    if numero <= 1:                               
        return numero                            
    else:                                    
        return fibonacci(numero-1)+fibonacci(numero-2)


name_1 = input()
ataque_1 = int(input())
defesa_1 = int(input())
ataque_especial_1 = int(input())
name_2 = input()
ataque_2 = int(input())
defesa_2 = int(input())
ataque_especial_2 = int(input())
vida = int(input())
vidaBase = vida * 100

vidas = combate(1, vidaBase, vidaBase, ataque_1, ataque_2, ataque_especial_1, ataque_especial_2, defesa_1, defesa_2, name_1, name_2, vidaBase)

if vidas[0] <= 0:
    print(f'O vencedor da luta foi {name_2}')
else:
    print(f'O vencedor da luta foi {name_1}')

