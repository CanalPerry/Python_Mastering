# EX-45

#number
def number():
    numero = int(input("Digite: "))
    return numero
#KM/sForM/s
def kmforms(numero):
    r = numero / 3.6
    return r
#M/sForKM/s
def msforkm(numero):
    r = numero * 3.6
    return r
#CodeHome
cont = True
while(cont == True):
    print("ESCOLHA:\n 1.KM/s para M/s\n 2. M/s para KM/s\n 3.SAIR")
    choice = number()
    if(choice == 1):
        print("KM/s: ")
        km = number()
        print(f"A conversão de {km}KM/s é {kmforms(km):.1f}M/s.")
    elif(choice == 2):
        print("M/s: ")
        ms = number()
        print(f"A conversão de {ms}M/s é {msforkm(ms):.1f}KM/s. ")
    elif(choice == 3):
        print("Program Finshed.")
        cont == False
    elif(choice != 1 and 2 and 3):
        print("Error 404")