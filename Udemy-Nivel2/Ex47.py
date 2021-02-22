# EX-47

#NUMBER
def number():
    numero = float(input("Digite: "))
    return numero
#ADIÇÃO
def adicao():
    print("R = X + Y")
    print("Valor de X:")
    x = number()
    print("Valor de Y:")
    y = number()
    r = x + y
    return print(f"{x} + {y} = {r}")
#SUBTRAÇÃO
def subtracao():
    print("R = X - Y")
    print("Valor de X:")
    x = number()
    print("Valor de Y:")
    y = number()
    r = x - y
    return print(f"{x} - {y} = {r}")
#DIVISÃO
def divisao():
    print("R = X / Y")
    print("Valor de X:")
    x = number()
    print("Valor de Y:")
    y = number()
    r = x / y
    return print(f"{x} / {y} = {r}")
#MULTPLICAÇÃO
def multplicacao():
    print("R = X * Y")
    print("Valor de X:")
    x = number()
    print("Valor de Y:")
    y = number()
    r = x * y
    return print(f"{x} * {y} = {r}")
#MENU
def menu(choice):
    if(choice == 1):
        adicao()
        return True
    elif(choice == 2):
        subtracao()
        return True
    elif(choice == 3):
        divisao()
        return True
    elif(choice == 4):
        multplicacao()
        return True
    elif(choice == 5):
        return False
    else:
        print("ERROR 404")
        return True
#CODEHOME
const = True
while(const == True):
    print("1.Adição\n2.Subtração\n3.Divisão\n4.Multiplicação\n5.Sair")
    choice = int(input("ESCOLHA: "))
    if(menu(choice) == False):
        const = False
        print("Program is finished")