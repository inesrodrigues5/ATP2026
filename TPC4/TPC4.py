import random
listaint=[]
def mostrar_menu():
    print("(1) Criar lista")
    print("(2) Ler lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem descrecente")
    print("(9) Procura um elemento")
    print("(0) Sair")
mostrar_menu()
opção=-1
while opção!=0:
    opção=int(input("Escreva a opção que deseja: "))
    if opção==0:
        print("Saiu da aplicação")
    elif opção==1:
        def criarLista(listaint):
            listaint=[]
            N=int(input("Escolha o número de elementos da lista: "))
            for i in range(N):
                listaint.append(random.randint(1,100))
            return listaint
        listaint=criarLista(listaint)
        print(criarLista(listaint))
    elif opção==2:
        def leLista(listaint):
            listaint=[]
            N=int(input("Escolha o número de elementos da lista: "))
            num=int
            for num in range(N):
                num=int(input("Escolha os elementos da lista: "))
                listaint.append(num)
                N=N-1
            return listaint
        listaint=leLista(listaint)
        print(listaint)
    elif opção==3:
        def somaLista(listaint):
            soma=0
            for n in listaint:
                soma=soma+n
            return soma
        print(somaLista(listaint))
    elif opção==4:
        def médiaLista(listaint):
            soma=0
            for n in listaint:
                soma=soma+n
                média=soma/len(listaint)
            return média
        print(médiaLista(listaint))
    elif opção==5:
        def maiorLista(listaint):
            maior=listaint[0]
            for n in listaint:
                if n>maior:
                    maior=n
            return(maior)
        print(maiorLista(listaint))
    elif opção==6:
        def menorLista(listaint):
            menor=listaint[0]
            for n in listaint:
                if n<menor:
                    menor=n
            return(menor)
        print(menorLista(listaint))
    elif opção==7:
        def estaOrdenadaporordemcrescente(listaint):
            for i in range(len(listaint)-1):
                if listaint[i]>listaint[i+1]:
                    return False
            return True
        if estaOrdenadaporordemcrescente(listaint):
            print("Sim")
        else:
            print("Não")
    elif opção==8:
        def estaOrdenadaporordemdecrescente(listaint):
            for i in range(len(listaint)-1):
                if listaint[i]<listaint[i+1]:
                    return False
            return True
        if estaOrdenadaporordemdecrescente(listaint):
            print("Sim")
        else:
            print("Não")
    elif opção==9:
        def procurarelemento(listaint):
            x=input("Qual o elemento que pretende procurar na lista?")
            for i in range(len(listaint)):
                if x==listaint[i]:
                    print("O elemento encontra-se na posição", i+1)
                else:
                    print("-1")
            return listaint
        
