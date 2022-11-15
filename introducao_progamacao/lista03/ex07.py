legendas = []
contador_ruidos = 0
total_ruidos = 0
for c in range(10):
    frase = input()
    if frase != 'tss' and frase != 'zzz': # vendo se não é composta so de ruidos
        # Vendo se tem ruido no final das frases
        if frase.split()[-1] == 'tss' or frase.split()[-1] == 'zzz':
            contador_ruidos += 1
            frase = frase.split()[0:-1] # Vai excluir o ultimo termo
            frase = ' '.join(frase)
        # Vendo so tem ruido no começo das frases
        if frase.split()[0] == 'tss' or frase.split()[0] == 'zzz':
            contador_ruidos += 1
            frase = frase.split()[1:] # Vai excluir o primeiro termo
            frase = ' '.join(frase)
        legendas.append(frase)
    # Vendo se a frase eh so ruidos
    else:
        contador_ruidos += 1
        total_ruidos += 1

if total_ruidos == 10:  # se a legenda foi so ruidos
    print('Eita, a legenda simplesmente inexiste! Tudo era ruido!')

else: # senao
    print('Legenda final:')
    print()
    for c in legendas:
        print(c)

    print()

    if (1 <= contador_ruidos <= 4) and (len(legendas) >= 8):
        print('Todo o ruido foi removido e voce mandou bem! A legenda saiu certinha. Pode subir!')
    elif contador_ruidos == 0:
        print('Nem precisava rodar, o audio ja estava limpinho e a legenda ta nos conformes. Marca o @billyraycyrus')
    elif (contador_ruidos > 4) or (len(legendas) < 8):
        print('Ih, tem alguma coisa errada com a legenda, ta estranha. Melhor dar uma verificada e regravar.')

