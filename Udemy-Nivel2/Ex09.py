# EX-09

#Ler número N
def number():
    x = int(input("Digite número: "))
    return x
#N primeiros números naturais impares
def impares(number):
    if(i % 2 == 1):
        return print(i)
#CodigoPrincipal
numberP = number()
for i in range(1, numberP):
    virifiimpar = impares(i)
