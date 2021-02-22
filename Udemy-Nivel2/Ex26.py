# EX-26

#LerNumero
def number():
    number = int(input("Digite numero: "))
    return number
#CodigoPrincipal
cont = True
max = number()
while(cont == True):
    if(max % 11 == 0 and max % 13 == 0 or max % 17 == 0):
        print(max)
        cont = False
    else:
        max += 1