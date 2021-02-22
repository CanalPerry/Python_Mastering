# EX-21

#LerNumero
def number():
    numero = int(input("Digite Numero: "))
    return numero
#SomaPar
def somaPar(number1, number2):
    soma = 0
    if(number1 > number2):
        for i in range(number2, number1):
            if(i % 2 == 0):
                soma += i
    else:
        for i in range(number1, number2):
            if(i % 2 == 0):
                soma += i
    return soma
#MultiplicaçãoImpar
def multiImpar(number1, number2):
    multi = 1
    if(number1 > number2):
        for i in range(number2, number1):
            if(i % 3 == 0):
                multi *= i
    else:
        for i in range(number1, number2):
            if(i % 3 == 0):
                multi *= i
    return multi
#CodigoPrincipal
numero1 = number()
numero2 = number()
multiimpar = multiImpar(numero1, numero2)
somapar = somaPar(numero1, numero2)
print("Todos os numero somados: ",somapar,"Todos os numeros multiplicados: ", multiimpar)