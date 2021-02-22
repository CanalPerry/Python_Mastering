# EX-24

#LerNumero
def number():
    number = int(input("Digite Numero: "))
    return number
#Divisores
def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            yield i
    yield num
#SomaDivisores
def somadiv(lista, number):
    max = 0
    for i in range(0, len(lista)):
            max += lista[i]
    return max
#CodigoPrincipal
numero = number()
lista = list(divisores(numero))
max = somadiv(lista, numero)
print("Esse são os divisores de ", numero, lista, " Esse é o numero somado de todos eles: ", max)
