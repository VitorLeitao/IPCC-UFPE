# Pontuações iniciais
acidez = 20
agua = 15
tempero = 10
continuar = True
while continuar == True:
    n = int(input())
    comando = input()
    if comando == 'reduzir agua':
        agua -= n
        tempero += (n - 1)
    elif comando == 'adicionar agua':
        agua += n
        tempero -= (n + 2)
    elif comando == 'reduzir acidez':
        acidez -= n
    elif comando == 'aumentar acidez':
        acidez += n
    elif comando == 'aumentar tempero':
        tempero += n

    if acidez == agua and agua == tempero and acidez == tempero:
        print('Tem sabor, tem apresentacion, tem tudibon! sobe no mezanin')
        continuar = False
    else:
        if acidez != agua and acidez != tempero and tempero != agua: # Tres diferentes
            if agua < acidez and agua < tempero:
                print('Muit seca! melhorre a combinaçon')
            elif acidez < agua and acidez < tempero:
                print('Falta acidez! non pode subir o mezanin')
            elif tempero < agua and tempero < acidez:
                print('Falta tomperro! non agradou meu paladar')
        else:
            if agua == acidez:
                if agua < tempero:
                    print('Muit seca! melhorre a combinaçon')
                    print('Falta acidez! non pode subir o mezanin')
                else:
                    print('Falta tomperro! non agradou meu paladar')
            elif agua == tempero:
                if agua < acidez:
                    print('Muit seca! melhorre a combinaçon')
                    print('Falta tomperro! non agradou meu paladar')
                else:
                    print('Falta acidez! non pode subir o mezanin')
            elif acidez == tempero:
                if acidez < agua:
                    print('Falta tomperro! non agradou meu paladar')
                    print('Falta acidez! non pode subir o mezanin')
                else:
                    print('Muit seca! melhorre a combinaçon')
