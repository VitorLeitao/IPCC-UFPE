def impar_par(num):
    global tipo
    if num == 0:
        tipo = 'par'
        return 0
        
    elif num == 1:
        tipo= 'impar'
        return 0
    
    return impar_par(num%2)

def fatorial(numero, prev):
    global analisar_fact
    if numero == 1:
        return 1
    a = numero * fatorial(numero - 1, prev)
    if a == prev:
        analisar_fact =  'sim'
    else:
        analisar_fact = 'nao'
    return a

# Comparando cada elemento da lista de primos com recursão
def primo(numero, index, contador):
    if (index == (len(lista) - 1)) or contador == 2:
        return contador
    if numero % lista[index] == 0:
        contador += 1
    
    return primo(numero, index + 1, contador)

contador_acertos = 0
contador_erros = 0
continuar = True
while continuar == True: 
    mensagem = input()
    # Caso a operação seja primo
    if mensagem == 'Primo':
        numero = int(input())
        if numero == 1:
            print(f'O número {numero} é primo, continue herói!')
            contador_erros = 0
            contador_acertos += 1
        else:
            # Lista de numeros primos ate o numero atual
            lista = []
            for c in range(1, (numero // 2) + 1):
                contador = 0
                for i in range(1, c + 1):
                    if c % i == 0:
                        contador += 1
                if contador <= 2:
                    lista.append(c)
            resultado = primo(numero,0, 0)
            if resultado <= 1:
                print(f'O número {numero} é primo, continue herói!')
                contador_erros = 0
                contador_acertos += 1
            else:
                print('Por aqui não.')
                contador_acertos = 0
                contador_erros += 1
    # Caso a operação seja somar
    elif mensagem == 'Somar':
        numeros = input()
        numero = 0
        for c in numeros:
            c = int(c)
            numero += c
        resultado = impar_par(numero)
        if tipo == 'par':
            print(f'O número {numero} é par, siga por aqui Link!')
            contador_erros = 0
            contador_acertos += 1
        else:
            print('Por aqui não.')
            contador_acertos = 0
            contador_erros += 1
    # Caso a operação seja Fatorial
    elif mensagem == 'Fatorial':
        numeros = input()
        num_1 = int(numeros.split()[0])
        num_2 = int(numeros.split()[-1])
        if (num_1 == 0) or (num_1 == 1):
            resultado = 1
            if num_2 == resultado:
                print(f'A resposta é mesmo {num_2} Link, esse caminho está certo!')
                contador_erros = 0
                contador_acertos += 1
            else:
                print('Por aqui não.')
                contador_acertos = 0
                contador_erros += 1
        else:
            resultado = fatorial(num_1, num_2)
            if analisar_fact == 'sim':
                print(f'A resposta é mesmo {num_2} Link, esse caminho está certo!')
                contador_erros = 0
                contador_acertos += 1
            else:
                print('Por aqui não.')
                contador_acertos = 0
                contador_erros += 1
    # Caso não seja nenhuma
    else:
        print('Por aqui não.')
        contador_acertos = 0
        contador_erros += 1

    # Olhando se acabou
    if contador_acertos >= 3:
        print('Com a sua ajuda o Link finalmente conseguiu sair do labirinto!!!')  
        continuar = False
    if contador_erros >= 3:
        print('Hoje não é um bom dia para o nosso herói...') 
        continuar = False





