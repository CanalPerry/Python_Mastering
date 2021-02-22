# EX-33

#lerNumeros
def number():
    numero = int(input('Digite numero: '))
    return numero
#Conta
def conta(n,i,j,lista):
    lista = []
    x = 0
    f = 0
    while(x < n):
        if(f % i == 0):
            lista.append(f)
            x += 1
        elif(f % j == 0):
            lista.append(f)
            x += 1
        f += 1
    return lista
#CodigoPrincipal
n = number()
i = number()
j = number()
lista = []
lista.append(conta(n,i,j,lista))
print(lista)