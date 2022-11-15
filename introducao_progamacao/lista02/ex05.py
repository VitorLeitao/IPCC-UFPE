numero_chefs = int(input())
numero_notas0 = 0
for c in range(0, numero_chefs):
    nome = input()
    nota_1 = float(input())
    nota_2 = float(input())
    nota_3 = float(input())
    media = (nota_1 + nota_2 + nota_3) / 3
    if media <= 0:
        numero_notas0 += 1

    if c == 0:
        nome_eliminado = nome
        nota_eliminado = media
    else:
        if media < nota_eliminado:
            nota_eliminado = media
            nome_eliminado = nome

if numero_notas0 > 0:
    print('Ocorreu um erro no sistema de notas, por favor insira notas validas')
else:
    print(f'O chef eliminado da vez é: {nome_eliminado} - {nota_eliminado:.2f}')


