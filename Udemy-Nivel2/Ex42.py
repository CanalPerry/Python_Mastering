# EX-42

import math
#Number
def number():
    number = int(input("Digite: "))
    return number
#Calculos
def calculos(number):
    quadrado = number**2
    cubo = number**3
    raiz = math.sqrt(number)
    return print(f" O número:{number}\n Quadrado:{quadrado}\n Cubo:{cubo}\n RaizQuadrada:{raiz}")
#CodigoHome
cont = True
while(cont == True):
    numero = number()
    if(numero < 0):
        cont = False
    else:
        calculos(numero)