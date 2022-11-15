dict_animais = {
    'avestruz' : ['01', '02', '03', '04'],
    'aguia': ['05', '06', '07', '08'],
    'burro': ['09', '10', '11', '12'],
    'borboleta': ['13', '14', '15', '16'],
    'cachorro': ['17', '18', '19', '20'],
    'cabra': ['21', '22', '23', '24'],
    'carneiro': ['25', '26', '27', '28'],
    'camelo': ['29', '30', '31', '32'],
    'cobra': ['33', '34', '35', '36'],
    'coelho': ['37', '38', '39', '40'],
    'cavalo': ['41', '42', '43', '44'],
    'elefante': ['45', '46', '47', '48'],
    'galo': ['49', '50', '51', '52'],
    'gato': ['53', '54', '55', '56'],
    'jacare': ['57', '58', '59', '60'],
    'leao': ['61', '62', '63', '64'],
    'macaco': ['65', '66', '67', '68'],
    'porco': ['69', '70', '71', '72'],
    'pavao': ['73', '74', '75', '76'],
    'peru': ['77', '78', '79', '80'],
    'touro': ['81', '82', '83', '84'],
    'tigre': ['85', '86', '87', '88'],
    'urso': ['89', '90', '91', '92'],
    'veado': ['93', '94', '95', '96'],
    'vaca': ['97', '98', '99', '00'],
}

lista_numeros = []
# PReenchendo a lista com numeros sorteados
for c in range(5):
    numero = input()
    numero = list(numero)
    lista_numeros.append(numero)

animal = input()
valor = int(input())
lista_numeros_animal = dict_animais[animal]
contido = False
for c in lista_numeros:
    for i in range(0, 3, 2):
        numero = ''
        numero += c[i]
        numero += c[i + 1]
        if numero in lista_numeros_animal:
            contido = True
            break
if contido == True:
    print(f'Parabens!!! Voce conseguiu ganhar {valor * 18} reais no jogo!!!')
else:
    print('Infelizmente nao foi dessa vez... Zeca pagodinho que acabou ganhando')

