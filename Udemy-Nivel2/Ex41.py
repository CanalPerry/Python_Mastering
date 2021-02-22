# EX-41

#NUMBER
def number():
    number = int(input("Digite: "))
    return number
#Resistência
def resistencia(r1, r2):
    r = (r1*r2)/(r1+r2)
    return r
#CodeHome
cont = True
while(cont == True):
    r1 = number()
    r2 = number()
    if(r1 and r2 != 0):
        print("R1:",r1,"R2:",r2,"é igual há:", resistencia(r1, r2))
    else:
        cont = False
        print("Finish Program")