# EX-32B

#LerQuantidadeDeVezes
import random
def vezes():
    vezes = int(input("Digite o numero: "))
    return vezes
#moeda
def moeda():
    lado = [0,1]
    aleatorio = random.choice(lado)
    return aleatorio
#CodigoPrincipal
cara = 0
coroa = 0
numero = vezes()
for i in range(1, numero+1):
    d1 = moeda()
    if(d1 == 0):
        cara += 1
    elif(d1 == 1):
        coroa += 1
print("Numero de vezes jogado: ", numero, "numero da cara: ", cara, "numerode coroa: ", coroa)