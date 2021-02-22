#EX-54

#VerificarNumeroPrimo
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
    return True
#Number
def number():
    numero = int(input("Digite: "))
    return numero
#CODEHOME
print("Digite um número para saber se ele é Primo :")
numero = number()
veri = primo(numero)
if(veri == True):
    print(f"{numero} É primo!")
else:
    print(f"{numero} Não é primo!")