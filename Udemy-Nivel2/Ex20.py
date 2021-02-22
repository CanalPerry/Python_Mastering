# EX-20

#LerNumero
def number():
    numbe = int(input("Digite o número: "))
    return numbe
#ImparOupar
def par(number):
    if(number % 2 == 0):
        return True
    else:
        return False
#CodigoPrincipal
print("Digite 1000 e pare o progrma.")
cont = True
valorLer = 0
parler = 0
while(cont == True):
    numero = number()
    if(par(numero) == True):
        valorLer += 1
        parler += 1
    else:
        valorLer += 1
    if(numero == 1000):
        cont = False
print("Numero dados Lidos: ", valorLer," Numero de par lidos: ", parler)
