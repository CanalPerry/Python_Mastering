# EX-27

#lerNumero
def number():
    number = int(input("Digite o numero: "))
    return number
#Harmonica
def harmonica(number):
    max = 0
    for i in range(1, number):
        max = max + 1/i
    return max
#CodigoPrincipal
numero= number()
harmonico = harmonica(numero)
print(harmonico)