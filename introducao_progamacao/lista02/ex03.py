numero_sairam = int(input())

for c in range(0, numero_sairam):
    nome = input()
    if nome == 'Prior':
         print('IIIHHH! El mago esta eliminado!')
    elif nome == 'Manu':
        print('Manu saiu! Bruna Marquezine deve estar muito triste :(')
    elif nome == 'Pyong':
        print('Agora o Pyong que dormiu, esta eliminado')
    elif nome == 'Gizelly':
        print('PPPPPYYYYYOOOONNNGGG LEEEEEE, Gizelly volta pra casa!')

    if c == 0:
        indicado_paredao = nome
    elif c == 18:
        lider = nome

print(f'- O indicado(a) ao paredao nessa semana e: {indicado_paredao}')
if numero_sairam == 19:
    print(f'- O novo lider da semana e: {lider}!')
else:
    restante = 19 - numero_sairam
    print(f'- Ainda restam {restante} pessoas na disputa pela lideranca!')