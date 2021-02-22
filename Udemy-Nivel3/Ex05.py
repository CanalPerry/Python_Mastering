#Crie um cadastro de Aluno Nome,Serie e CPF
#Aluno
def Aluno():
    nome = input("Digite nome: ")
    serie = input("Digite serie: ")
    CPF = int(input("Digite CPF: "))
    return nome, serie, CPF
#CodePrincipal
list = []
n1 = int(input("Digite o numero de alunos: "))
for i in range(0, n1):
    x = (Aluno())
    list.append(x)
for i in range(0, n1):
    print(list[i])
