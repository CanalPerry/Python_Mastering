# EX-30

#LerNumero
def number():
    number = int(input("Digite o Numero: "))
    return number
#FirstSequencia
def first(number):
    max = 0
    for i in range(1, number):
        max += i
    return max
#SecondSequencia
def second(number):
    max = 0
    for i in range(1, number):
        max = max + (2 * i - 1)
    return max
#CodigoPrincipal
numero = number()
primeiro = first(numero)
segundo = second(numero)
print("This is first: ", primeiro, "This is second: ", segundo)