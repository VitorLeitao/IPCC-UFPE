x_bulma = int(input())
y_bulma = int(input())
raio_radar = int(input())
x_esfera = int(input())
y_esfera = int(input())
if raio_radar > 0:
    raio_esfera = 2
    raio_detectavel = raio_radar + raio_esfera
    distancia = ((x_bulma - x_esfera)**2 + (y_bulma - y_esfera)**2) ** 0.5
    if raio_detectavel >= distancia:
        print('Esferas do dragao detectadas')
    else:
        print('Esferas fora do radar')
else:
    print('Sua amplitude esta baixa, nao conseguimos te localizar no radar')


