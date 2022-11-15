chegada = int(input())
soma = 0
continua = True
while continua == True:
    num = int(input())
    if num < 0:
        continua = False
    else:
        for c in range(0, num):
            soma += (c + 1)

if soma < chegada:
    print('Ainda nos falta um pouco...')
elif soma == chegada:
    print('Pode beijar a noiva, afinal, vocês conseguiram!')
elif chegada < soma < (chegada * 20):
    print('Parece que os pombinhos passaram um pouco do local...')
elif (chegada * 20) <= soma <= (chegada * 100):
    print('Acho que nos perdemos um pouco no caminho, onde estamos?')
else:
    print('Hum... acho que o casal deve rever seus votos de matrimônio...')

