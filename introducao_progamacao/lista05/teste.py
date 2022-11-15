matriz = [
    ['#', '#', '#'],
    ['.', '#', '.'],
    ['#', 'L', '#']
]

for c in range(len(matriz)):
            for i in range(len(matriz[c])):
                if i ==(len(matriz[c]) - 1):
                    print(f'{matriz[c][i]}')
                else:
                    print(f'{matriz[c][i]}',end='')
            