# EX-32

#LerQuantidadeDeVezes
import random
def vezes():
    vezes = int(input("Digite o numero: "))
    return vezes
#Dado
def dado():
    lado = [1, 2, 3, 4, 5, 6]
    aleatorio = random.choice(lado)
    return aleatorio
#CodigoPrincipal
numero = vezes()
for i in range(1, numero):
    d1 = dado()
    d2 = dado()
    if(d1 > d2):
        print("No lançamento: ", i, "d1 é maior que d2")
    elif(d1 == d2):
        print("No lançamento: ", i, "d1 é igual a d2")
    elif(d1 < d2):
        print("No lançamento: ", i, "d1 é menor que d2")