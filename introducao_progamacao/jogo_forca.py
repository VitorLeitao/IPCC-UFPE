"""
 Jogo da forca
"""


# Leitura da palavra e do numero de turnos.
word = input('digite a palavra a ser usada na forca(a palavra não pode conter numeros ou alfanumericos): ').strip().lower()
turns_limit = int(input('digite o numero máximo de turnos para a forca: '))
size = len(word)

while turns_limit < size:  # While pra caso o numero de turnos for irregular.
    print('o numero de turnos é menor que a quantidade de letras! digite novamente.')
    turns_limit = int(input('digite o numero máximo de turnos para a forca: '))

print("\x1b[2J")
list_letters = []  # Lista feita pra determinar se a letra foi repetida / no final sera usado para mostrar a palavra.
print(f'a palavra tem {size} letras, vamos começar a forca!')
hits = turns = total_num = 0

# While pro numero de turnos determinados,  cada um contendo uma letra.O codigo analisa se ela esta ou não na palavra.
while True:

    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    # Leitura da letra
    letter = input('digite uma letra: ').strip().lower()

    if letter in word and letter not in list_letters:  # Caso a letra esteja na palavra pre-determinada e não tenha sido usada ainda.

        num = int(word.count(letter))
        print(f'\na letra {letter} esta presente na palavra numa quantidade de {num}.')
        list_letters.append(letter)
        hits = hits + num  # Variavel acumuladora para o total de acertos GERAL.
        hits_missing = size - hits

        print(f'\nvoce ainda precisa acertar {hits_missing} letras.')

    elif letter in word and letter in list_letters:  # Caso a letra esteja na palavra, porem ja tenha sido usada.
        print(f'\na letra {letter} ja foi digitada e não contabilizada nos acertos.')

    elif letter not in word and letter not in list_letters:  # Caso a letra nãoa esteja na palavra.
        print(f'\na letra não esta presente na palavra.')

    print(f'\nvoce tem um total de {hits} acertos!')
    turns = turns + 1

    # Digitação da palavra, mostrando '-' caso a letra ainda não tenha sido digitada.
    print(f'\npalavra: ')
    for c in range(0, size):
        if word[c] in list_letters:
            print(word[c], end='')
        else:
            print('-', end='')

    # Quebrar o while caso os turnos ultrapassem o limte de turnos determinado, ou seja, derrota.
    if turns_limit <= turns:
        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('não foi dessa vez, tente novamente mais tarde!')
        break

    # Quebrar o while, caso o numero de acertos seja do tamanho da palavra, ou seja, vitória.
    if hits == size:
        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'\nparabens!! voce chegou ao fim, num total de {turns} turnos.', end=' ')
        break






