palavra = 'PROVA-DO-ANJO-BBB'
letras_certas = ''  # Vai armazenas todas as letras que ja foram digitadas e estao presentes na palavra certa
letras = ''  # Vai armazenar todas as letras que ja foram digitadas
vidas = 3
while vidas > 0:
    letra = str(input()).upper()
    # olhando se a letra ja foi digitada
    contador_1 = 0
    for c in letras:
        if c == letra:
            contador_1 += 1
    if contador_1 > 0:
        print(f'Voce ja digitou a letra {letra}')
        print(palavra_digitada)
    else:
        letras += letra
        # Olhando se a letra digitada pertence a palavra
        contador_2 = 0
        for c in palavra:
            if c == letra and letra != '-':
                letras_certas += letra
                contador_2 += 1

        # Se não a letra não estiver na palvra
        if contador_2 == 0:
            vidas -= 1
            if vidas == 0:
                print('Fim de jogo, sem almoco do anjo pra voce!')
            else:
                print(f'Que pena, voce tem mais {vidas} chances!')
                palavra_digitada = ''  # Palavra que será digitada pro usuario
                for c in palavra:
                    contador_3 = 0
                    for i in letras_certas:
                        if i == c:
                            contador_3 += 1
                    if contador_3 > 0:
                        palavra_digitada += f'{c}'
                    else:
                        palavra_digitada += '-'
                print(palavra_digitada)

        # Se a letra estiver na palavra
        else:
            palavra_digitada = ''  # Palavra que será digitada pro usuario
            for c in palavra: #PROVA-DO-ANJO-BBB
                contador_4 = 0
                for i in letras_certas:
                    if i == c:
                        contador_4 += 1
                if contador_4 > 0:
                    palavra_digitada += f'{c}'
                else:
                    palavra_digitada += '-'
            if palavra_digitada == palavra:
                print('Parabens, voce conseguiu mais uma letra!')
                print(palavra_digitada)
                print('Boa, voce e o novo Anjo da semana!')
                vidas = 0
            else:
                print('Parabens, voce conseguiu mais uma letra!')
                print(palavra_digitada)












