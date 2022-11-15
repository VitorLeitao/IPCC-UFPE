# Função busca bonaria
def busca_binaria(lista, elemento, inicio, fim):
    if 'Ghost Potrificationizer - E. Gadd' in lista:
        meio = inicio + (fim - inicio) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            return busca_binaria(lista, elemento, inicio, meio - 1)
        else:
            return busca_binaria(lista, elemento, meio + 1, fim)
    else:
        return -1
# Função para colocar o poder de tras pra frente
def mudar_posicao(numero):
    numero = str(numero)
    numero = list(numero)
    novo_numero = []
    for c in range(len(numero)-1,-1,-1):
        novo_numero.append(numero[c])
    # Transformando lista em string e dps em int
    numero_str = ''
    for c in novo_numero:
        c = str(c)
        numero_str += c
    numero_final = int(numero_str)
    return numero_final
# Função para ver se é Capicua
def capiuca(numero):
    novo_numero = numero + mudar_posicao(numero)
    novo_numero = str(novo_numero)
    novo_numero = list(novo_numero)
    numero_inverso = []
    for c in range(len(novo_numero)-1,-1,-1):
        numero_inverso.append(novo_numero[c])
    # Caso base
    if novo_numero == numero_inverso:
        numero_str = ''
        for c in novo_numero:
            c = str(c)
            numero_str += c
        numero_int = int(numero_str)
        return numero_int
    numero_str = ''
    for c in novo_numero:
        c = str(c)
        numero_str += c
    numero_int = int(numero_str)
    return capiuca(numero_int)

estante = []
num = int(input())
for c in range(num):
    livro = input()
    estante.append(livro)

poder = busca_binaria(estante, 'Ghost Potrificationizer - E. Gadd', 0, num) + 1
poder = poder * 7
poder_final = capiuca(poder)
if poder_final == 0:
    print('Mamma mia! Só Mario poderá me salvar agora!')
elif poder_final < 50:
    print('É uma catástrofe, eu tenho a arma mas só posso usá-la uma vez')
elif 50 <= poder_final < 100:
    print('Terei que usar a minha arma com sabedoria!')
elif 100 <= poder_final < 200:
    print('A arma está bem carregada, me dei bem!')
else:
    print('Aha! EU NÃO TENHO MAIS MEDO DE NADA! PODEM VIR!')
