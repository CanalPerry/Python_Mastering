# EX-13&&EX-14&&EX-15&&EX-16

#LerNumeroInteiro
def number():
    numero = int(input("Digite número: "))
    return numero
#Positivo
def positivo(number):
    if(number > 0):
        return True
    else:
        return False
#OrdemCrescentePar
def crescentePar(number):
    for i in range(0, number):
        if(i % 2 == 0):
            print(i)
#OrdemDecrescentePar
def descrescentePar(number):
    for i in range(number, -1, -1):
        if(i % 2 == 0):
            print(i)
#OrdemCrescenteImpar
def crescenteImpar(number):
    for i in range(1, number):
        if(i % 2 == 1):
            print(i)
#OrdemDecrescenteImpar
def decrescenteImpar(number):
    for i in range(number, -1, -1):
        if(i % 2 == 1):
            print(i)
#CodigoPrincipal
cont = True
while(cont == True):
    numeroP = number()
    if(positivo(numeroP)== True):
        print("Ordem Crescente PAR:")
        crespar = crescentePar(numeroP)
        print("Ordem Decrescente PAR:")
        decrespar = descrescentePar(numeroP)
        print("Ordem Crescente IMPAR:")
        cresimpar = crescenteImpar(numeroP)
        print("Ordem Decrescente IMPAR:")
        decresimpar = decrescenteImpar(numeroP)
        cont = False
    else:
        cont = True
