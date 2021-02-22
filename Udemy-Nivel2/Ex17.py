# EX-17

#LerNumeroInteiro
def number():
    x = int(input("Digete numero: "))
    return x
#Positivo
def positivo(number):
    if(number > 0):
        return True
    else:
        return False
#SomaNumeros
#NumerosPrimario
def soma(number):
    atual = 0
    for i in range(0, number):
        atual += i
    return atual
#CodigoPrincipal
cont = True
atual = 0
numberP = number()
while(cont == True):
    if(positivo(numberP) == True):
        atual = soma(numberP)
        cont = False
    else:
        cont = True
print(atual)
