# EX-19

#LerNumeroInterio100e999
def number():
    verif = True
    while(verif == True):
        number = int(input("Digite Número: "))
        if(number >= 100) and (number <= 999):
            return number
            verif = False
#RetornaNumeroEmLista
def lista(x):
    true = list(str(x))
    return true
#NumeroAleatorio
def numberAle(x):
        true = (len(x))
        if(true >= 2):
            print(x[1])
#CodigoPrincipal
numberP = number()
listaP = lista(numberP)
show = numberAle(listaP)