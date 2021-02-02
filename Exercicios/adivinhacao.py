print('******************************')
print('* Jogo da adivinhação        *')
print('******************************')
numero_secreto = 42
total_de_tentativas = 3
rodada = 1


while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!")
        break
    elif(maior):
        print("Você Errou! O Numero que você chutou foi maior que o numero secreto")

    elif(menor):
        print("Você Errou! O Numero que você chutou foi menor que o numero secreto")

    rodada = rodada + 1
    print('Fim do jogo')