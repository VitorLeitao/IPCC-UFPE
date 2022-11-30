# Ned Leeds e os vilões

vilao_1 = input()
poder_1 = int(input())
local_1 = int(input())

vilao_2 = input()
poder_2 = int(input())
local_2 = int(input())

if poder_1 < 0 or poder_2 < 0:
    print('Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.')
else:
    destruicao_1 = ((poder_1 ** 2) * local_1) / 2
    destruicao_2 = ((poder_2 ** 2) * local_2) / 2
    if destruicao_1 > destruicao_2:
        print(f'Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao_1}.')
    elif destruicao_2 > destruicao_1:
        print(f'Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao_2}.')
    else:
        if destruicao_1 % 2 == 0:
            print('E quem disse que isso e problema meu? Vou chamar o senhor Stark.')
        else:
            print('Vou chamar uns reforcos de outro universo... rsrs')
