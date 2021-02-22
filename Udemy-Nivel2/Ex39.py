# EX-39
#NUmber
def number():
    x = True
    while (x == True):
        number = int(input("Digite: "))
        if(number > 0):
            x = False
            return number
        else:
            print("Erro 404")
#AreaTriangulo
def areatriangulo(x, y):
    a = (x * y)/2
    return a
#CodeHome
print("Digite base e altura: ")
x = number()
y = number()
print("A area do triangulo é: ", areatriangulo(x, y))