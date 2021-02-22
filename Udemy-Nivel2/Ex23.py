# EX-23

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
#CodigoPrincipal
numero = number()
lista = list(divisores(numero))
print("Os divisores dele são: ", lista)