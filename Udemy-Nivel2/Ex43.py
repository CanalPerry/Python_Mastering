# EX-43

#Number
def number():
    number = int(input("Digite: "))
    return number
#media
def media(soma, quantidade):
    media = soma / quantidade
    return media
#CodeHome
soma = 0
quantidade = 0
cont = True
while(cont == True):
    idade = number()
    if(idade > 0):
        soma += idade
        quantidade += 1
    else:
        cont = False
print("Há media é: ", media(soma, quantidade))