# EX-40

#Number
def number():
    number = int(input("Digite: "))
    return number
#Verifik
def verifik(number):
    if(number < 0):
        return True
    else:
        return False
#MostraMaior
def showinghight(atual, maior):
    if(atual > maior):
        atual = maior
        return atual
    else:
        return maior
#CodeHome
cont = True
maior = 0
while(cont == True):
    novo = number()
    if(verifik(novo)== False):
        maior = showinghight(maior, novo)
    else:
        cont = False
print("O maior número digitado é: ", maior)