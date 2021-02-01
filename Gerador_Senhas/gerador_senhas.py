import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%"
pergunta = "s"

all = lower + upper + numbers + symbols
while (pergunta == "s"):
    try:
        print("******* Software para Gerar Senhas em Python - Rosner ********")
        length = int(input("Número de caracteres da senha: "))
        password = "".join(random.sample(all,length))
        print(password)
        pergunta = input("Gerar outra senha? s/n. ")

    except ValueError:
        print("Somente numeros sao aceitos. Tente novamente.")
        pergunta = input("Deseja Continuar? s/n. ")