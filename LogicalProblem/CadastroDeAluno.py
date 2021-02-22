# Faça um sistema de cadastro de aluno, com Nome,serie,sala,Idade.
# E o sistema de Notas de 6 Materias, Matematica,Historia,Português,Inglês ,Arte,ED.Fisica.
# Onde você coloca as 4 notas de bimestres e que saia a media.


##CADASTRO DE NOME,SERIE,SALA,IDADE.

import random
def cadastro(aluno):
    aluno = []
    nome = input("Digite Nome do Aluno: ")#STRING
    idade = int(input("Digite Idade do Aluno: "))
    serie = int(input("Digite Serie do Aluno: "))
    sala = input("Digite Sala do Aluno: ").upper()
    cpf = int(input("Digite CPF: "))
    y = ''
    for i in range(0, 5):
        x = random.randrange(0, 9)  # define the range of the primes
        y = y + str(x)
    print(f"SEU RA: {y}")
    aluno.append(y)
    aluno.append(f"Nome:{nome}")
    aluno.append(f"Idade:{idade}")
    aluno.append(f"Serie:{serie}")
    aluno.append(f"Sala:{sala}")
    aluno.append(f"CPF:{cpf}")
    return aluno


##VERICAR CADASTRO
def verifik(aluno):
    cont = 0
    x = 0
    most = True
    print("----- A  L  U  N O -------")
    RA = int(input("Digite o RA: "))
    RA = str(RA)
    for i in range(0, len(aluno)):
        if aluno[i][x] == RA:
            x = i
            while most == True:
                if cont == 0:
                    print(f"RA: {aluno[x][0]}")
                    cont += 1
                elif cont == 1:
                    print(aluno[x][1])
                    cont += 1
                elif cont == 2:
                    print(aluno[x][2])
                    cont += 1
                elif cont == 3:
                    print(aluno[x][3])
                    cont += 1
                elif cont == 4:
                    print(aluno[x][4])
                    cont += 1
                elif cont == 5:
                    print(aluno[x][5])
                    cont += 1
                elif cont >= 6:
                    most = False


##ADICIONAR NOTAS
def add(lista):
    n1 = int(input("Nota do 1°Bimestre: "))
    n2 = int(input("Nota do 2°Bimestre: "))
    n3 = int(input("Nota do 3°Bimestre: "))
    n4 = int(input("Nota do 4°Bimestre: "))
    media = (n1 + n2 + n3 + n4) / 4
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    lista.append(n4)
    lista.append(media)
    return lista


##CHECAR TUDO JUNTO E MISTURADO....
def checar(lista, RA, materias):
    most = True
    n = 0
    print("----- A  L  U  N O -------")
    for i in range(0, len(aluno)):
        if aluno[i][n] == RA:
            RA = i
    while(most == True):
        print(f"RA: {lista[RA][0]}")
        print(lista[RA][1])
        print(lista[RA][2])
        print(lista[RA][3])
        print(lista[RA][4])
        print(lista[RA][5])
        ##MATEMATICA
        print(f"Nota de {materias[0]}")
        print(f"1°Bimestre:{lista[RA][6][0]}")
        print(f"2°Bimestre:{lista[RA][6][1]}")
        print(f"3°Bimestre:{lista[RA][6][2]}")
        print(f"4°Bimestre:{lista[RA][6][3]}")
        print(f"Media:{lista[RA][6][4]}")
        ##HISTORIA
        print(f"Nota de {materias[1]}")
        print(f"1°Bimestre:{lista[RA][6][5]}")
        print(f"2°Bimestre:{lista[RA][6][6]}")
        print(f"3°Bimestre:{lista[RA][6][7]}")
        print(f"4°Bimestre:{lista[RA][6][8]}")
        print(f"Media:{lista[RA][6][9]}")
        ##PORTUGUÊS
        print(f"Nota de {materias[2]}")
        print(f"1°Bimestre:{lista[RA][6][10]}")
        print(f"2°Bimestre:{lista[RA][6][11]}")
        print(f"3°Bimestre:{lista[RA][6][12]}")
        print(f"4°Bimestre:{lista[RA][6][13]}")
        print(f"Media:{lista[RA][6][14]}")
        ##INGLÊS
        print(f"Nota de {materias[3]}")
        print(f"1°Bimestre:{lista[RA][6][15]}")
        print(f"2°Bimestre:{lista[RA][6][16]}")
        print(f"3°Bimestre:{lista[RA][6][17]}")
        print(f"4°Bimestre:{lista[RA][6][18]}")
        print(f"Media:{lista[RA][6][19]}")
        ##ARTE
        print(f"Nota de {materias[4]}")
        print(f"1°Bimestre:{lista[RA][6][20]}")
        print(f"2°Bimestre:{lista[RA][6][21]}")
        print(f"3°Bimestre:{lista[RA][6][22]}")
        print(f"4°Bimestre:{lista[RA][6][23]}")
        print(f"Media:{lista[RA][6][24]}")
        ##ED.FISICA
        print(f"Nota de {materias[5]}")
        print(f"1°Bimestre:{lista[RA][6][25]}")
        print(f"2°Bimestre:{lista[RA][6][26]}")
        print(f"3°Bimestre:{lista[RA][6][27]}")
        print(f"4°Bimestre:{lista[RA][6][28]}")
        print(f"Media:{lista[RA][6][29]}")
        most = False
x = []
aluno = []
materias = ["Matemática", "Historia", "Português", "Inglês", "Arte", "ED.Fisica"]
cont = True
most = True
n = 0
while(cont == True):
    print("1 - CADASTRAR ALUNO")
    print("2 - CHECAR ALUNO")
    escolha = int(input("DIGITE O QUE VOCÊ QUER FAZER: "))
    if(escolha == 1):
        aluno.append(cadastro(x))
        print(verifik(aluno))
        print("--------NOTAS-----------")
        RA = int(input("Digite o RA: "))
        RA = str(RA)
        for i in range(0, len(aluno)):
            if aluno[i][n] == RA:
                RA = i
                for i in range(0, len(materias)):
                    print(f"NOTA DE {materias[i]}")
                    aluno[RA].append(add(x))
    elif(escolha == 2):
        print("---FICHA DO ALUNO----")
        RA = int(input("Digite o RA: "))
        RA = str(RA)
        for i in range(0, len(aluno)):
            if (aluno[i][n] == RA):
                checar(aluno, RA, materias)
    print("----------S   A  I  R-----------\n--------------------------------")
    sair = input("   DESEJA SAIR: ").upper()
    if sair == "SAIR":
        cont = False
    else:
        cont = True