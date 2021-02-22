# EX-46

#Number
def number():
    numero = int(input("Digite: "))
    return numero
#Verificar
def arroz(aleatorio, numero):
    if(numero == aleatorio):
        return True
    else:
        return False
#MaiorMenor
def maiormenor(aleatorio, numero):
    if(aleatorio > numero):
        return print("MAIOR")
    else:
        return print("MENOR")
#CodeHome
import random
lista = []
const = True
tenta = 0
for i in range(1, 1000+1):
    lista.append(i)
print(lista)
aleatorio = random.choice(lista)
print(aleatorio)
while(const == True):
    numero = number()
    if(arroz(aleatorio, numero) == True):
        const = False
    else:
        maiormenor(aleatorio, numero)
    tenta += 1
print(f"Numero de tentativa: {tenta}\nNumero Aleatorio: {aleatorio}\nNumero: {numero}")
