

secreto = 'cozinheira'
digitadas = []
chances = 3

print('-='* 20)
print('               JOGO DA FORCA PYTHON')
print('-='* 20)

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Você só pode digitar apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Parabens, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'VOCÊ GANHOU! a palavra secreta era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()