letra = input()
numero = int(input())
if numero < 0 or numero % 2 == 0:
    print('Entrada não permitida')
elif letra != 'T' and letra != 'X' and letra != 'O':
    print('Entrada não permitida')

else:
    # Imprimindo a letra T
    if letra == 'T':
        for c in range(0, numero):
            if c == 0:
                print('X' * numero)
            else:
                vezes_0 = '0' * (numero//2)
                print(f'\n{vezes_0}X{vezes_0}')

    # Imprimindo a letra O
    if letra == 'O':
        for c in range(0, numero):
            if c == 0:
                vezes_x = 'X' * numero
                print(f'{vezes_x}\n')
            elif c == (numero - 1):
                vezes_x = 'X' * numero
                print(f'{vezes_x}')
            else:
                vezes_0 = '0' * (numero - 2)
                print(f'X{vezes_0}X\n')

    # Imprimindo a letra X
    if letra == 'X':
        for c in range(0, numero):
            # Imprimindo a primeira e ultima linha do X
            if c == 0:
                vezes_0_extremidades = ''
                vezes_0 = '0' * (numero - 2)
                print(f'X{vezes_0}X\n')

            elif c == (numero - 1):
                vezes_0 = '0' * (numero - 2)
                print(f'X{vezes_0}X')

            # Imprimindo o termo medio
            elif c == (numero - 1)/2:
                vezes_0_extremidades = '0' * (numero // 2)
                print(f'{vezes_0_extremidades}X{vezes_0_extremidades}\n')

            # Imprimindo as linhas entre (1) o termo inicial e o termo medio (2) o termo medio e o termo final
            else:
                # Imprimindo a segunda parte do X (2)
                if c > (numero // 2):
                    vezes_0_extremidades = '0' * (len(vezes_0_extremidades) - 1)
                    vezes_0 = '0' * (numero - ((len(vezes_0_extremidades) * 2) + 2))
                    print(f'{vezes_0_extremidades}X{vezes_0}X{vezes_0_extremidades}\n')
                # Imprimindo a primeira parte do X (1)
                else:
                    vezes_0_extremidades = '0' * (len(vezes_0_extremidades) + 1)
                    vezes_0 = '0' * (numero - ((len(vezes_0_extremidades) * 2) + 2))
                    print(f'{vezes_0_extremidades}X{vezes_0}X{vezes_0_extremidades}\n')




