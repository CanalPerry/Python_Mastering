#EX-55 && 56 && 57 && 58

#NUmber
def number():
    const = True
    while(const == True):
        number = int(input("Digite: "))
        if(number < 0):
            print("Erro 404")
        else:
            const = False
            return number
#VerifikarPrimo
def primo(number):
    if(number <= 1):
        return False
    elif(number <= 3):
        return True
    elif(number % 2 == 0 or number % 3 == 0):
        return False
    i = 5
    while(i * i <= number):
        if(number % i == 0 or number % (i + 2) == 0):
            return False
        i += 6
    return True
#LaçoParaNprimeiroNUmero
def lacoN(number):
    z = 0
    for i in range(0, number):
        if(primo(i) == True):
            z += i
    return z
#SomaDeTodosAté2M
def soma():
    const = True
    z = 0
    m = 0
    while(const == True):
        z += 1
        if(primo(z) == True and z < 2000000):
            m += z
        elif(z == 2000000):
            const = False
    return m
#ContarA&&B
def AandB(a, b):
    z = 0
    for i in range(a, b):
        if(primo(i) == True):
            z += 1
    return z
#SOMAA&B
def somaAandB(a, b):
    z = 0
    for i in range(a, b):
        if(primo(i) == True):
            z += i
    return z
#CodeHome
num = number()
print(f"O valor do numero: ", lacoN(num))
print(f"Soma de todos os primos até 2M é {soma()}")
a = number()
b = number()
print(f"De A a B: {AandB(a, b)}\n Soma A and B:{somaAandB(a, b)}")