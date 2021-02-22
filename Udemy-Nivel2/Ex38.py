# EX-38

import math
#Pitagoras
def raiz(x, y):
    a = x**2 + y**2
    toti = math.sqrt(a)
    return toti
#NUMBER
def number():
    number = int(input("Digite: "))
    return number
#CodeHome
print("Valor de A ")
x = number()
print("Valor de B ")
y = number()
print("A hipotenusa é: ", raiz(x, y))