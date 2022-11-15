lista = []
continuar = True
while continuar == True:
    passo = input()
    if passo == 'FIM':
        continuar = False
    else:
        lista.append(passo)


print(f'Olá seguimores! O primeiro passo da dancinha é {lista[0]}')
print(f'Depois, a gente faz o {lista[1]} e {lista[2]}')
x = len(lista[2:-1])
print(f'Temos ainda mais {x} passos pra aprender!')
print(f'Por último, vamos fazer o {lista[-1]}')
