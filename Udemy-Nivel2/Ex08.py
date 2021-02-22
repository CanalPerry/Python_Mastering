# EX-08

#Escrever 10 números
def number():
    x = int(input("Digite Numero: "))
    return x
#Escrever o Menor número
def minoria(number, menor):
    if(menor == 0):
        return number
    if(number <= menor):
        return number
    else:
        return menor

#Escrever o Maior número
def maioral(number, maior):
    if(number >= maior):
        return number
    else:
        return maior
#CodigoPrincipal
menor = 0
maior = 0
cont = 0
while(cont < 10):
    numberP = number()
    maior = maioral(numberP, maior)
    menor = minoria(numberP, menor)
    cont += 1
print("Maior: ", maior, "Menor: ", menor)