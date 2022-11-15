contador = 0
var = 0
while True:
    if (contador % 11 == 4) and (contador % 13 == 9):
        print(contador)
        var += 1
        if var == 3:
            break
    contador += 1