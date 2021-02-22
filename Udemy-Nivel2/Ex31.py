# EX-31

#LerNumero
def number():
    numero = int(input("Digite o numero: "))
    return numero
#CalculoDeS
def calculoS(number):
    max = 0
    for i in range(1, number):
        max = max + ((2 * i - 1)/i)
    return max
#CodigoPrincipal
numero = number()
maximo = calculoS(numero)
print("This is calculator of S: ", maximo)