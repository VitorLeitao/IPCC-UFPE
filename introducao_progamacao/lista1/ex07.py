#CInFlix

categoria = input()
genero = input()
if categoria == 'Serie':
    if genero == 'Acao':
        conteudo = 'The Boys'

    if genero == 'Terror':
        conteudo = 'A Maldicao da Residencia Hill'

    if genero == 'Drama':
        conteudo = 'Euphoria'

    if genero == 'Aventura':
        conteudo = 'The Witcher'

    if genero == 'Romance':
        conteudo = 'Bridgerton'

    if genero == 'Animacao':
        conteudo = 'Arcane'

    if genero == 'Comedia':
        conteudo = 'FRIENDS'

    if genero == 'Fantasia':
        conteudo = 'Game Of Thrones'

    if genero == 'Suspense':
        conteudo = 'Prison Break'

    if genero == 'Policial':
        conteudo = 'Peaky Blinders'

    if genero == 'Ficcao':
        conteudo = 'Dark'

    print(f'{conteudo} e a serie mais popular do genero {genero} no momento.')

if categoria == 'Filme':
    if genero == 'Acao':
        conteudo = 'Kill Bill Vol. I'

    if genero == 'Terror':
        conteudo = 'It - A Coisa'

    if genero == 'Drama':
        conteudo = 'Sempre ao Seu Lado'

    if genero == 'Aventura':
        conteudo = 'Homem - Aranha: Sem Volta para Casa'

    if genero == 'Romance':
        conteudo = 'Me Chame Pelo Seu Nome'

    if genero == 'Animacao':
        conteudo = 'Encanto'

    if genero == 'Comedia':
        conteudo = 'Nao Olhe Para Cima'

    if genero == 'Fantasia':
        conteudo = 'Harry Potter e a Pedra Filosofal'

    if genero == 'Suspense':
        conteudo = 'Corra!'

    if genero == 'Policial':
        conteudo = 'Cidade de Deus'

    if genero == 'Ficcao':
        conteudo = 'Interestelar'

    print(f'{conteudo} e o filme mais popular do genero {genero} no momento.')


