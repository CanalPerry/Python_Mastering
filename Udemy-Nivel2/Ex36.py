# EX-36

#LerNumeros
def number():
    numero = int(input("Digite o número: "))
    return numero
#SomaDosNumeroElevadosAoQuadrado
def somaquadrado(n):
    z = 0
    for i in range(1, n+1):
        z += i**2
    return z
#SomaDosNumerosEDepoisElevadoAoQuadrado
def somabefore(n):
    z = 0
    for i in range(1, n+1):
        z += i
    z = z**2
    return z
#CodigoPrincipal
numero = number()
somaq = somaquadrado(numero)
somab = somabefore(numero)
x = somab - somaq
print(x)