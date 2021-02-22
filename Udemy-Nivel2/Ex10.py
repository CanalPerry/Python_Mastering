# EX-10

#AleatorioNumberPar
def aleatorio(number):
    for i in range(0, number):
        return i
#Receber number
def number():
    number = int(input("Digite número: "))
    return number
#Soma Number Par
def soma(atual, number):
    atual += number
    return atual
#Par
def par(number):
    if(number % 2 == 0):
        return True
    else:
        return False
#CodigoPrincipal
cont = 0
atualprimario = 0
while(cont <= 50 ):
    numberP = number()
    if(par(numberP) == True):
        atualprimario = soma(atualprimario, numberP)
        cont += 1
print("O valor total é: ", atualprimario)
#CodigoSecundario
contS = 0
atualsecundario = 0
numberS = number()
while(contS <= 50):
    aleato = aleatorio(numberS)
    if(par(aleato) == True):
        atualsecundario = soma(atualsecundario, numberS)
        contS += 1
print("O valor total é: ", atualsecundario)
