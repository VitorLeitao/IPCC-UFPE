
empresa_1 = input()
empresa_2 = input()
empresa_3 = input()
dict = {}
while True:
    try:
        infos = input().split()
        if infos[0] in dict:
            print(f'{infos[0]} ja esta participando da avaliacao!')
        elif not ((infos[2] == empresa_1) or (infos[2] == empresa_2) or (infos[2] == empresa_3)):
            print(f'Nao ha ligacoes entre {infos[0]} e as empresas concorrentes, prossiga tranquilamente com a entrevista.')
        else:
            dict_candidato = {
                'idade' : int(infos[1]),
                'empresa' : infos[2],
                'anos trabalhados' : int(infos[-1])
            }
            dict[infos[0]] = dict_candidato
    except:
        break

print('[ALERTA]! A SEGUIR UMA LISTA DOS POSSIVEIS ESPIOES')
for c in dict:
    print(f'{c}:')
    idade = dict[c]['idade']
    print(f'- Idade: {idade}')
    empresa = dict[c]['empresa']
    print(f'- Antiga corporacao: {empresa}')
    anos_trabalho = dict[c]['anos trabalhados']
    print(f'- Anos trabalhos: {anos_trabalho}')
    # Calculando probabilidade
    prob = (anos_trabalho / idade) * 100
    if (idade >= 50) and (prob >= 30):
        if empresa == empresa_1:
            prob = prob * 1.15
        elif empresa == empresa_2:
            prob = prob * 1.1
        else:
            prob = prob * 1.05
    elif (idade <= 30) and (prob >= 40):
        if empresa == empresa_1:
            prob = prob * 1.3
        elif empresa == empresa_2:
            prob = prob * 1.25
        else:
            prob = prob * 1.2

    else:
        if (prob > 20):
            if empresa == empresa_1:
                prob = prob * 1.1
            elif empresa == empresa_2:
                prob = prob * 1.05
            else:
                prob = prob * 1.03
    
    print(f'- Probabilidade de ser espiao: {int(prob)}%')


