numero_festas = int(input())
mensagem = ''
# Variaveis contadoras do total de bebida de TODAS AS FESTAS
numero_cerveja_total = 0
numero_caipirinha_total = 0
numero_vodca_total = 0

for c in range(0, numero_festas):
    numero_copos = int(input())
    # Variaveis contadoras do total de bebida de CADA FESTA
    numero_cerveja = 0
    numero_caipirinha = 0
    numero_vodca = 0
    # Computando a quantidade de copos de cada bebida
    for i in range(0, numero_copos):
        bebida = input()
        if bebida == 'cerveja':
            numero_cerveja += 1
            numero_cerveja_total += 1
        elif bebida == 'caipirinha':
            numero_caipirinha += 1
            numero_caipirinha_total += 1
        elif bebida == 'vodca':
            numero_vodca += 1
            numero_vodca_total += 1

    # Calculando a bebida que o maluco mais tomou na festa
    max = numero_cerveja
    nome_max = 'cerveja'
    if numero_caipirinha > max:
        max = numero_caipirinha
        nome_max = 'caipirinha'
    if numero_vodca > max:
        max = numero_vodca
        nome_max = 'vodca'

    # Registrando a bebida que o maluco mais tomou em uma variavel
    mensagem += f'O que ele mais tomou nessa festa foi: {nome_max}\n'

# imprimindo as bebidas mais tomadas por festa
print(mensagem, end='')

# Imprimindo o total de copos que ele tomou pra cada bebida
print(f'cerveja - {numero_cerveja_total}')
print(f'caipirinha - {numero_caipirinha_total}')
print(f'vodca - {numero_vodca_total}')





