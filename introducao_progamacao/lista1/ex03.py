# The office

nome = input()
valor_semestre1 = int(input())
valor_semestre2 = int(input())
media = (valor_semestre1 + valor_semestre2) // 12

if nome == 'Jim Halpert' or nome == 'Dwight Schrute' or nome == 'Phyllis Vance' or nome == 'Stanley Hudson':
    if media <= 50:
        frase = f'{nome}, voce so vendeu {media} por mes? Voce ta demitido... Brincadeira!'
    if 50 < media < 100:
        frase = f'{nome}, voce mandou mal... Vai ter que pagar meu almoco.'
    if media >= 100:
        frase = f'Parabens, {nome}! Voce foi promovido! kkkkk Brincadeira, a matriz que decide!'
    print(frase)
else:
    print('Sinto muito, mas so os vendedores eh que vao ganhar a viagem pra matriz.')