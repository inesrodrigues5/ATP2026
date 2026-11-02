nome = ""
id = 0
notaTPC = 0
notaProj = 0
notaTeste = 0
aluno = (nome,id,[notaTPC,notaProj,notaTeste])
turma = []
def mostrar_menu():
    print("(1) Criar uma turma")
    print("(2) Inserir um aluno na turma")
    print("(3) Listar a turma")
    print("(4) Consultar um aluno por id")
    print("(8) Guardar a turma em ficheiro")
    print("(9) Carregar uma turma dum ficheiro")
    print("(0) Sair da aplicação")
mostrar_menu()
numero=-1
while numero!=0:
    numero=int(input("Escolha uma das opções: "))
    if numero==1:
        def Criarturma(turma):
            return[]
        print("Turma criada")
    elif numero==2:
        def Inseriraluno(turma):
            nome=str(input("Nome: "))
            id=int(input("id: "))
            notaTPC=float(input("NotaTPC: "))
            notaProj=float(input("NotaProj: "))
            notaTeste=float(input("NotaTeste: "))
            turma.append((nome, id, [notaTPC, notaProj, notaTeste]))
            return(turma)
        turma=Inseriraluno(turma)
    elif numero==3:
        def Listarturma(turma):
            if len(turma) == 0:
                print("A turma está vazia.")
            for aluno in turma:
                print(aluno)
        Listarturma(turma)
    elif numero==4:
        def Encontraralunoporid(turma):
            id=int(input("id: "))
            encontrado = None
            for aluno in turma:
                if aluno[1]==id:
                    encontrado=aluno
            return(encontrado)
        aluno = Encontraralunoporid(turma)
        if aluno is None:
            print("Aluno não encontrado.")
        else:
            print("Aluno encontrado:", aluno)
    elif numero==8:
        def Guardaraturmaemficheiro(turma):
            nomef = input("Nome do ficheiro: ")
            f = open(nomef, "w")
            for aluno in turma:
                f.write(f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n")
            f.close()
        Guardaraturmaemficheiro(turma)
        print("Turma guardada")
    elif numero==9:
        def Carregarumaturmadumficheiro():
            res= []
            f = open(turma, "r")
            for linha in f:
                campos = linha.strip().split(",")
                nome = campos[0]
                id_aluno = int(campos[1])
                notaTPC = float(campos[2])
                notaProj = float(campos[3])
                notaTeste = float(campos[4])
                aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
                res.append(aluno)
            f.close()
            return res
        print("Turma carregada")
    if numero==0:
        print("Saiu da aplicação")