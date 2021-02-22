# EX-22

#lerNumero
def number():
    number = int(input("Digite o numero: "))
    return number
#Intervalo10a20
def interval(number):
    if(number >= 10 and number <= 20):
        return True
    else:
        return False
#MediaAritmetica
def aritimetica(number, media):
    valor = number/media
    return valor
#CodigoPrincipal
print("Digite um numero entre 10 e 20.\nPara sair do loop digite um numero fora do 10 e 20.")
cont = True
media = 0
max = 0
while(cont == True):
    numero = number()
    if(interval(numero) == True):
       max += numero
       media += 1
    else:
        cont = False
print(aritimetica(max, media))