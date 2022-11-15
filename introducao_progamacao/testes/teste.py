import random
lista = ['Vitor','Lucas','duda','Gabriel','marina','Igor','França',' geovana', 'joão','Gabriel gama', 'Luana','mel','maju','João Marrocos','Felipe','Guilherme','artur', 'sofia']

times = {
}
for c in range(3):
    time = []
    for i in range(6):
        escolha = random.choice(lista)
        time.append(escolha)
        index = lista.index(escolha)
        lista.pop(index)
    times[c] = time

for c in range(3):
    print(times[c])
