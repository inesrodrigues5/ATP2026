print("Corrida para o 100: O total começa em 0. O jogador e o computador alternam somando um número de 1 a 10 ao total. Quem atingir exatamente o número 100 vence.")
modalidade=int(input("escolha a modalidade que deseja jogar(1 - o computador começa ou 2 - o jogador começa): "))
import random
total=0
if modalidade==1:
    x=1
    while total<100:
        print("o computador escolheu o numero: ", x)
        y=int(input("escolha um numero: "))
        total=total+x+y
        print("total = ", total)
        if total==100:
            print("O computador ganhou")
        if total<100:
            x=11-y
if modalidade==2:
    x=0
    while total<100:
        y=int(input("escolha um número: "))
        total=total+y
        print("total = ", total)
        if total==100:
            print("O jogador ganhou!")
        if total<100:
            x=11-y
            print("o computador escolheu o número: ", x)
            total=total+x
            print("total: ", total)
            if total==100:
                print("O computador ganhou")