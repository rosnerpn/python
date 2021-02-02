print('******************************')
print('* Jogo da adivinhação        *')
print('******************************')
numero_secreto = 42
total_de_tentativas = 3
rodada = 1
pontos = 1000
print("Ponto Inicial: {}".format(pontos))
nivel = int(input("Digite o nivél do Jogo - 1 = 20 tentativas - 2 = 10 tentativas - 3 = 5 tentativas: "))


if (nivel ==1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
elif (nivel == 3):
    total_de_tentativas = 5


while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print('Você digitou: ', chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!")
        pontos = pontos - abs(numero_secreto - chute)
        print("Seus Pontos: {}".format(pontos))
        print("")
        break
    elif(maior):
        print("Você Errou! O Numero que você chutou foi maior que o numero secreto")
        pontos = pontos - abs(numero_secreto - chute)
        print("Seus Pontos: {}".format(pontos))
        print("")

    elif(menor):
        print("Você Errou! O Numero que você chutou foi menor que o numero secreto")
        pontos = pontos - abs(numero_secreto - chute)
        print("Seus Pontos: {}".format(pontos))
        print("")

    rodada = rodada + 1
   