
modalidade=int(input("escolha a modalidade que deseja jogar(1 ou 2): "))
import random
if modalidade==1:
    resposta=random.randint(0,100)
    x=int(input("escreva um número entre 0 e 100 "))
    tentativas=1
    while x!=resposta:
        if x<resposta:
            print("o número que pensei é maior")
        elif x>resposta:
            print("o número que pensei é menor")
        x=int(input("escreva outro número entre 0 e 100 "))
        tentativas=tentativas+1
    print("acertou; o número de tenativas:", tentativas)
elif modalidade==2:
    print("adivinha um número entre 0 e 100")
    x=random.randint(0,100)
    print(x)
    resposta=str(input("resposta(acertou; o número que pensei é maior; o número que pensei é menor): "))
    tentativas=1
    minimo=0
    maximo=100
    while resposta!="acertou":
        if resposta=="o número que pensei é maior":
            minimo=x
            x=random.randint(minimo,maximo)
        elif resposta=="o número que pensei é menor":
            maximo=x
            x=random.randint(minimo,maximo)
        tentativas=tentativas+1
        print(x)
        resposta=str(input("resposta(acertou; o número que pensei é maior; o número que pensei é menor): "))
    print("Número de tentativas: ", tentativas)
