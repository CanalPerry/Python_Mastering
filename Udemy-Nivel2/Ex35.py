# EX-35

#LerNumero
def number():
    numero = int(input("Digite o número: "))
    return numero
def calculo(ini, fin):
    z = 0
    for i in range(ini, fin+1):
        if(i % 3 == 0):
            z += i
    return z
#CodigoPrincipal
cont = True
while(cont == True):
    print("Valor inicial ")
    inicial = number()
    print("Valor Final ")
    final = number()
    if(final < inicial):
        print("Erro Digite um valor valido.")
    elif(final > inicial):
        print("Essa é a soma dos Impares", calculo(inicial, final))
        cont = False