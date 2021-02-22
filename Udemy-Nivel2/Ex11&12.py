# EX-11&& EX-12

#Ler Numero Inteiro
def number():
    numero = int(input("Digite número: "))
    return numero
#NumeroPositivo
def positivo(number):
    if(number >= 0):
        return True
    else:
        return False
#Ordem Crescente
def crescente(number):
    for i in range(0, number+1):
        print(i)
#Ordem Decrescente
def decrescente(number):
    for i in range(number, -1, -1):
        print(i)
#CodigoPrincipal
cont = True
while(cont == True):
    numeroP = number()
    if(positivo(numeroP) == True):
        print("Ordem Crescente:")
        cresc = crescente(numeroP)
        print("Ordem Decrescente:")
        decresc = decrescente(numeroP)
        cont = False
    else:
        cont = True
