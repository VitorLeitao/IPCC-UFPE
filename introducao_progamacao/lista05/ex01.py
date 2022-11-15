# FUnção pra retornar o mdc. obs: num_1 tem que ser maior que numero 2
def mdc(num_1, num_2):
    resto = num_1 % num_2
    if resto == 0:
        return num_2
    
    return mdc(num_2, resto)

lista_numeros = []
for c in range(3):
    num = int(input())
    lista_numeros.append(num)

# COlocando em ordem, pois a função precisa disso
lista_numeros = sorted(lista_numeros)
mdc_1 = mdc(lista_numeros[-1], lista_numeros[1])
if mdc_1 >= lista_numeros[0]:
    mdc_2 = mdc(mdc_1, lista_numeros[0])
else:
    mdc_2 = mdc(lista_numeros[0], mdc_1)

# output
if mdc_2 == 1:
    print('Infelizmente apenas 1 treinador pokemon ira receber os itens hoje, e com certeza nao e o atrasado do Ash.')
else:
    print(f'Gracas a Companhia Pokemon, {mdc_2} treinadores pokemon vao receber itens do Professor!')