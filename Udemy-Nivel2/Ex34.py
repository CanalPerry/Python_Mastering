# EX-34

#lerNumero
def number():
    numero = int(input("Digite numero: "))
    return numero
#Calculo
def conta(n):
    lista = []
    x = 1
    f = 0
    while(x < 20):
        if(f % n == 0):
            lista.append(f)
            x += 1
        f += 1
    return lista
#CodigoPrincipal
numero = number()
lista = []
lista.append(conta(numero))
print(lista)