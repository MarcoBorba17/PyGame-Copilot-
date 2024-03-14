import random

# Lista de palavras para o jogo
palavras = ['python', 'java', 'javascript', 'programacao', 'hacker']

# Escolhe uma palavra aleatória da lista
palavra_secreta = random.choice(palavras).upper()
palavra_display = ['_' for i in palavra_secreta]

# Número de chances do jogador
chances = 6

# Jogo da forca
print('Bem-vindo ao Jogo da Forca!')
print(' '.join(palavra_display))

while chances > 0 and '_' in palavra_display:
    palpite = input('Digite uma letra: ').upper()

    if palpite in palavra_secreta:
        # Revela a letra na palavra_display
        for index, letra in enumerate(palavra_secreta):
            if letra == palpite:
                palavra_display[index] = letra
    else:
        # Reduz as chances se a letra não estiver na palavra
        chances -= 1
        print(f'Letra incorreta. Você tem {chances} chances restantes.')

    # Mostra o estado atual da palavra
    print(' '.join(palavra_display))

# Verifica se o jogador ganhou ou perdeu
if '_' not in palavra_display:
    print('Parabéns, você ganhou!')
else:
    print(f'Você perdeu! A palavra era: {palavra_secreta}')