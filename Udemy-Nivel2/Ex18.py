# EX-18

#LerNumero
def number():
    number = int(input("Digite Numero: "))
    return number
#Maior
def maior(number, maior):
    if(number >= maior):
        return number
    else:
        return maior
#CodigoPrincipal
print("Digite o Valor total dos numeros: ")
cont = number()
maio = 0
x = 0
atual = 0
while(x <= cont):
    numero = number()
    if(maio == 0):
        maio = numero
    atual = maior(numero, maio)
    x += 1
print("Maior: ", atual, "Contagem lido: ", x)