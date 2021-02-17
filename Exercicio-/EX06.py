# EX-01
'''
x = 3
b = 0
contagem = 1
while(b < 5):
    verdade = contagem % 3
    if(verdade == 0):
        b += 1
        print(contagem)
    contagem += 1

'''
# EX-02
'''
print("FOR")
for i in range(100+1):
    print(i)
x = 1
print("WHILE")
while(x < 100):
    x += 1
    print(x)
'''

# EX-03
'''
x = 10
while(x >= 0):
    print(x)
    x-=1
print("LANÇAR!!!")
'''

# EX-04
'''
x = int(input("Digite um Número:"))
for i in range(0, x*100000, x*1000):
    print(i)
'''
# EX-05
'''
x = 0
count = 0
while(x < 10):
    number = int(input("Digite o Número: "))
    count = count + number
    x += -1
print(count)
'''
# EX-06
'''
x = 0
count = 0
while(x < 10):
    number = int(input("Digite O Número: "))
    count += number
    x += 0
print(count/9)
'''
# EX-07
'''
x = 0
count = 0
while(x < 10):
    number = int(input("Digite o Número: "))
    if(number >= 0):
        count += number
        x += 1
print(count/10)
'''
# EX-08
'''
#Escrever 10 números
def number():
    x = int(input("Digite Numero: "))
    return x
#Escrever o Menor número
def minoria(number, menor):
    if(menor == 0):
        return number
    if(number <= menor):
        return number
    else:
        return menor

#Escrever o Maior número
def maioral(number, maior):
    if(number >= maior):
        return number
    else:
        return maior
#CodigoPrincipal
menor = 0
maior = 0
cont = 0
while(cont < 10):
    numberP = number()
    maior = maioral(numberP, maior)
    menor = minoria(numberP, menor)
    cont += 1
print("Maior: ", maior, "Menor: ", menor)
'''
# EX-09
'''
#Ler número N
def number():
    x = int(input("Digite número: "))
    return x
#N primeiros números naturais impares
def impares(number):
    if(i % 2 == 1):
        return print(i)
#CodigoPrincipal
numberP = number()
for i in range(1, numberP):
    virifiimpar = impares(i)
'''
# EX-10
'''
#AleatorioNumberPar
def aleatorio(number):
    for i in range(0, number):
        return i
#Receber number
def number():
    number = int(input("Digite número: "))
    return number
#Soma Number Par
def soma(atual, number):
    atual += number
    return atual
#Par
def par(number):
    if(number % 2 == 0):
        return True
    else:
        return False
#CodigoPrincipal
cont = 0
atualprimario = 0
while(cont <= 50 ):
    numberP = number()
    if(par(numberP) == True):
        atualprimario = soma(atualprimario, numberP)
        cont += 1
print("O valor total é: ", atualprimario)
#CodigoSecundario
contS = 0
atualsecundario = 0
numberS = number()
while(contS <= 50):
    aleato = aleatorio(numberS)
    if(par(aleato) == True):
        atualsecundario = soma(atualsecundario, numberS)
        contS += 1
print("O valor total é: ", atualsecundario)
'''
# EX-11&& EX-12
'''
#Ler Numero Inteiro
def number():
    numero = int(input("Digite número: "))
    return numero
#NumeroPositivo
def positivo(number):
    if(number >= 0):
        return True
    else:
        return False
#Ordem Crescente
def crescente(number):
    for i in range(0, number):
        print(i)
#Ordem Decrescente
def decrescente(number):
    for i in range(number, -1, -1):
        print(i)
#CodigoPrincipal
cont = True
while(cont == True):
    numeroP = number()
    if(positivo(numeroP) == True):
        print("Ordem Crescente:")
        cresc = crescente(numeroP)
        print("Ordem Decrescente:")
        decresc = decrescente(numeroP)
        cont = False
    else:
        cont = True
'''
# EX-13&&EX-14&&EX-15&&EX-16
'''

#LerNumeroInteiro
def number():
    numero = int(input("Digite número: "))
    return numero
#Positivo
def positivo(number):
    if(number > 0):
        return True
    else:
        return False
#OrdemCrescentePar
def crescentePar(number):
    for i in range(0, number):
        if(i % 2 == 0):
            print(i)
#OrdemDecrescentePar
def descrescentePar(number):
    for i in range(number, -1, -1):
        if(i % 2 == 0):
            print(i)
#OrdemCrescenteImpar
def crescenteImpar(number):
    for i in range(1, number):
        if(i % 2 == 1):
            print(i)
#OrdemDecrescenteImpar
def decrescenteImpar(number):
    for i in range(number, -1, -1):
        if(i % 2 == 1):
            print(i)
#CodigoPrincipal
cont = True
while(cont == True):
    numeroP = number()
    if(positivo(numeroP)== True):
        print("Ordem Crescente PAR:")
        crespar = crescentePar(numeroP)
        print("Ordem Decrescente PAR:")
        decrespar = descrescentePar(numeroP)
        print("Ordem Crescente IMPAR:")
        cresimpar = crescenteImpar(numeroP)
        print("Ordem Decrescente IMPAR:")
        decresimpar = decrescenteImpar(numeroP)
        cont = False
    else:
        cont = True
'''
# EX-17
'''
#LerNumeroInteiro
def number():
    x = int(input("Digete numero: "))
    return x
#Positivo
def positivo(number):
    if(number > 0):
        return True
    else:
        return False
#SomaNumeros
#NumerosPrimario
def soma(number):
    atual = 0
    for i in range(0, number):
        atual += i
    return atual
#CodigoPrincipal
cont = True
atual = 0
numberP = number()
while(cont == True):
    if(positivo(numberP) == True):
        atual = soma(numberP)
        cont = False
    else:
        cont = True
print(atual)
'''
# EX-18
'''
#LerNumero
def number():
    number = int(input("Digite Numero: "))
    return number
#Maior
def maior(number, maior):
    if(number >= maior):
        return number
    else:
        return maior
#CodigoPrincipal
print("Digite o Valor total dos numeros: ")
cont = number()
maio = 0
x = 0
atual = 0
while(x <= cont):
    numero = number()
    if(maio == 0):
        maio = numero
    atual = maior(numero, maio)
    x += 1
print("Maior: ", atual, "Contagem lido: ", x)
'''
# EX-19
'''
#LerNumeroInterio100e999
def number():
    verif = True
    while(verif == True):
        number = int(input("Digite Número: "))
        if(number >= 100) and (number <= 999):
            return number
            verif = False
#RetornaNumeroEmLista
def lista(x):
    true = list(str(x))
    return true
#NumeroAleatorio
def numberAle(x):
        true = (len(x))
        if(true >= 2):
            print(x[1])
#CodigoPrincipal
numberP = number()
listaP = lista(numberP)
show = numberAle(listaP)
'''
# EX-20
'''
#LerNumero
def number():
    numbe = int(input("Digite o número: "))
    return numbe
#ImparOupar
def par(number):
    if(number % 2 == 0):
        return True
    else:
        return False
#CodigoPrincipal
cont = True
valorLer = 0
parler = 0
while(cont == True):
    numero = number()
    if(par(numero) == True):
        valorLer += 1
        parler += 1
    else:
        valorLer += 1
    if(numero == 1000):
        cont = False
print("Numero dados Lidos: ", valorLer," Numero de par lidos: ", parler)
'''
# EX-21
'''
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
'''
# EX-22
'''
#lerNumero
def number():
    number = int(input("Digite o numero: "))
    return number
#Intervalo10a20
def interval(number):
    if(number >= 10 and number <= 20):
        return True
    else:
        return False
#MediaAritmetica
def aritimetica(number, media):
    valor = number/media
    return valor
#CodigoPrincipal
cont = True
media = 0
max = 0
while(cont == True):
    numero = number()
    if(interval(numero) == True):
       max += numero
       media += 1
    else:
        cont = False
print(aritimetica(max, media))
'''
# EX-23
'''
#LerNumero
def number():
    number = int(input("Digite Numero: "))
    return number
#Divisores
def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            yield i
    yield num
#CodigoPrincipal
numero = number()
lista = list(divisores(numero))
print("Os divisores dele são: ", lista)
'''
# EX-24
'''
#LerNumero
def number():
    number = int(input("Digite Numero: "))
    return number
#Divisores
def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            yield i
    yield num
#SomaDivisores
def somadiv(lista, number):
    max = 0
    for i in range(0, len(lista)):
        if(lista[i] != number):
            max += lista[i]
    return max
#CodigoPrincipal
numero = number()
lista = list(divisores(numero))
max = somadiv(lista, numero)
print("Esse são os divisores de ", numero, lista, " Esse éo numero somado de todos eles: ", max)
'''
# EX-25
'''
#CodigoPrincipal
max = 0
for i in range(1000, -1, -1):
    if(i % 3 == 0 and i % 5 == 0):
        max += i
print(max)
'''
# EX-26
'''
#LerNumero
def number():
    number = int(input("Digite numero: "))
    return number
#CodigoPrincipal
cont = True
max = number()
while(cont == True):
    if(max % 11 == 0 and max % 13 == 0 or max % 17 == 0):
        print(max)
        cont = False
    else:
        max += 1
'''
# EX-27
'''
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
'''
# EX-28&&29
'''
maxone = 1
maxtwo = 2
E = 0
for i in range(0, 4):
    E = E + maxone/maxtwo
    maxone += 1
    maxtwo += 2
print(E)
'''
# EX-30
'''
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
'''
# EX-31
'''
#LerNumero
def number():
    numero = int(input("Digite o numero: "))
    return numero
#CalculoDeS
def calculoS(number):
    max = 0
    for i in range(1, number):
        max = max + ((2 * i - 1)/i)
    return max
#CodigoPrincipal
numero = number()
maximo = calculoS(numero)
print("This is calculator of S: ", maximo)
'''
# EX-32
'''
#LerQuantidadeDeVezes
import random
def vezes():
    vezes = int(input("Digite o numero: "))
    return vezes
#Dado
def dado():
    lado = [1, 2, 3, 4, 5, 6]
    aleatorio = random.choice(lado)
    return aleatorio
#CodigoPrincipal
numero = vezes()
for i in range(1, numero):
    d1 = dado()
    d2 = dado()
    if(d1 > d2):
        print("No lançamento: ", i, "d1 é maior que d2")
    elif(d1 == d2):
        print("No lançamento: ", i, "d1 é igual a d2")
    elif(d1 < d2):
        print("No lançamento: ", i, "d1 é menor que d2")
'''
# EX-32B
'''
#LerQuantidadeDeVezes
import random
def vezes():
    vezes = int(input("Digite o numero: "))
    return vezes
#moeda
def moeda():
    lado = [0,1]
    aleatorio = random.choice(lado)
    return aleatorio
#CodigoPrincipal
cara = 0
coroa = 0
numero = vezes()
for i in range(1, numero+1):
    d1 = moeda()
    if(d1 == 0):
        cara += 1
    elif(d1 == 1):
        coroa += 1
print("Numero de vezes jogado: ", numero, "numero da cara: ", cara, "numerode coroa: ", coroa)
'''
# EX-33
'''
#lerNumeros
def number():
    numero = int(input('Digite numero: '))
    return numero
#Conta
def conta(n,i,j,lista):
    lista = []
    x = 0
    f = 0
    while(x < n):
        if(f % i == 0):
            lista.append(f)
            x += 1
        elif(f % j == 0):
            lista.append(f)
            x += 1
        f += 1
    return lista
#CodigoPrincipal
n = number()
i = number()
j = number()
lista = []
lista.append(conta(n,i,j,lista))
print(lista)
'''
# EX-34
'''
#lerNumero
def number():
    numero = int(input("Digite numero: "))
    return numero
#Calculo
def conta(n):
    lista = []
    x = 1
    f = 0
    while(x < 20):
        if(f % n == 0):
            lista.append(f)
            x += 1
        f += 1
    return lista
#CodigoPrincipal
numero = number()
lista = []
lista.append(conta(numero))
print(lista)
'''
# EX-35
'''
#LerNumero
def number():
    numero = int(input("Digite o número: "))
    return numero
def calculo(ini, fin):
    z = 0
    for i in range(ini, fin+1):
        if(i % 3 == 0):
            z += i
    return z
#CodigoPrincipal
cont = True
while(cont == True):
    print("Valor inicial ")
    inicial = number()
    print("Valor Final ")
    final = number()
    if(final < inicial):
        print("Erro Digite um valor valido.")
    elif(final > inicial):
        print("Essa é a soma dos Impares", calculo(inicial, final))
        cont = False
'''
# EX-36
'''
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
'''
# EX-37
'''
??????
'''
# EX-38
'''
import math
#Pitagoras
def raiz(x, y):
    a = x**2 + y**2
    toti = math.sqrt(a)
    return toti
#NUMBER
def number():
    number = int(input("Digite: "))
    return number
#CodeHome
print("Valor de A ")
x = number()
print("Valor de B ")
y = number()
print("A hipotenusa é: ", raiz(x, y))
'''
# EX-39
'''
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
'''
# EX-40
'''
#Number
def number():
    number = int(input("Digite: "))
    return number
#Verifik
def verifik(number):
    if(number < 0):
        return True
    else:
        return False
#MostraMaior
def showinghight(atual, maior):
    if(atual > maior):
        atual = maior
        return atual
    else:
        return maior
#CodeHome
cont = True
maior = 0
while(cont == True):
    novo = number()
    if(verifik(novo)== False):
        maior = showinghight(maior, novo)
    else:
        cont = False
print("O maior número digitado é: ", maior)
'''
# EX-41
'''
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
'''
# EX-42
'''
import math
#Number
def number():
    number = int(input("Digite: "))
    return number
#Calculos
def calculos(number):
    quadrado = number**2
    cubo = number**3
    raiz = math.sqrt(number)
    return print(f" O número:{number}\n Quadrado:{quadrado}\n Cubo:{cubo}\n RaizQuadrada:{raiz}")
#CodigoHome
cont = True
while(cont == True):
    numero = number()
    if(numero < 0):
        cont = False
    else:
        calculos(numero)
'''
# EX-43
'''
#Number
def number():
    number = int(input("Digite: "))
    return number
#media
def media(soma, quantidade):
    media = soma / quantidade
    return media
#CodeHome
soma = 0
quantidade = 0
cont = True
while(cont == True):
    idade = number()
    if(idade > 0):
        soma += idade
        quantidade += 1
    else:
        cont = False
print("Há media é: ", media(soma, quantidade))
'''
# EX-44
'''
numero = 30
antigo = 0
novo = 1
resultado = 0
l1 = 0
l2 = 1
fibonnaci = []
fibonnaci.append(antigo)
fibonnaci.append(novo)
cont = True
while(cont == True):
    if(fibonnaci[l2] < numero):
        r = fibonnaci[l1] + fibonnaci[l2]
        fibonnaci.append(r)
        l1 += 1
        l2 += 1
    else:
        cont = False
print(fibonnaci)
'''
# EX-45
'''
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
#CodeHome
cont = True
while(cont == True):
    print("ESCOLHA:\n 1.KM/s para M/s\n 2. M/s para KM/s\n 3.SAIR")
    choice = number()
    if(choice == 1):
        print("KM/s: ")
        km = number()
        print(f"A conversão de {km}KM/s é {kmforms(km)}M/s.")
    elif(choice == 2):
        print("M/s: ")
        ms = number()
        print(f"A conversão de {ms}M/s é {msforkm(ms)}KM/s. ")
    elif(choice == 3):
        print("Program Finshed.")
        cont == False
    elif(choice != 1 and 2 and 3):
        print("Error 404")
'''
# EX-46
'''
#Number
def number():
    numero = int(input("Digite: "))
    return numero
#Verificar
def arroz(aleatorio, numero):
    if(numero == aleatorio):
        return True
    else:
        return False
#MaiorMenor
def maiormenor(aleatorio, numero):
    if(aleatorio > numero):
        return print("MENOR")
    else:
        return print("MAIOR")
#CodeHome
import random
lista = []
const = True
tenta = 0
for i in range(1, 1000+1):
    lista.append(i)
print(lista)
aleatorio = random.choice(lista)
print(aleatorio)
while(const == True):
    numero = number()
    if(arroz(aleatorio, numero) == True):
        const = False
    else:
        maiormenor(aleatorio, numero)
    tenta += 1
print(f"Numero de tentativa: {tenta}\nNumero Aleatorio: {aleatorio}\nNumero: {numero}")
'''
# EX-47
'''
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
'''
# EX-48
'''
def fibonnaci():
    fibolist = [0, 1]
    l1 = 0
    l2 = 1
    soma = 0
    fim = 4000000000
    const = True
    while(const == True):
        while(fibolist[l2] <= fim):
            r = fibolist[l1] + fibolist[l2]
            fibolist.append(r)
            l1 += 1
            l2 += 1
            if(fibolist[l2] % 2 == 0):
                soma += fibolist[l2]
        const = False
    print(soma)
    print(fibolist)
fibonnaci()
'''
# EX-49
'''
?????
'''
# EX-50
'''
Chico = 150
Ze = 110
Ano = 0
const = True
while(const == True):
    Chico += 2
    Ze += 3
    if(Ze > Chico):
        const = False
    Ano += 1
print(f"Durara {Ano} anos para Zé ficar maior que chico.\nTamanho de Zé: {Ze} m\nTamanho de Chico: {Chico}.")
'''
# EX-51
'''
quantidade = 2021 - 1996
x = 0
salario = 2000
porcentagem = 1.05
while(x <= quantidade):
     salario *= porcentagem
     print(porcentagem)
     x += 1
print(f"O salario atual dele é {salario:.2f} em {x} anos")
'''
# EX-52
'''
# Aproximação
def aproxi(nota, saque):
    ghost = []
    true = []
    for i in range(0, len(nota)):
        r = saque - nota[i]
        ghost.append(r)
    for i in range(0, len(ghost)):
        if (ghost[i] <= saque and ghost[i] >= 0):
            true.append(nota[i])
    return true
#Contagem
def contagem(contag, saque, estrutura):
    const = True
    nota = 0
    lista = []
    contag = contag[::-1]
    print(contag)
    x = 0
    b = 0
    for i in range(0, len(contag)):
        if(estrutura >= contag[i]):
            while(const == True):
                if(contag[i] <= saque):
                    estrutura = estrutura - contag[i]
                    if(estrutura < contag[i] and not estrutura == contag[i]):
                        const = False
                nota += 1
                x += 1
            if(x > b):
                lista.append(f"Foram {nota} nota de {contag[i]}")
                b += 1
            if(estrutura == 0):
                break
            else:
                const = True
            nota = 0
    return lista
#Number
def number():
    numero = int(input("Digite: "))
    return numero
#CODEHOME
nota = [1, 2, 5, 10, 20, 50, 100]
saque = number()
contag = aproxi(nota, saque)
r = contagem(contag, saque, saque)
print(r)
'''
#EX-53
'''
#NUMBER
def number():
    numero = int(input("Digite: "))
    return numero
#CODEHOME
n = 0
z = 0
v = 0
for i in range(1, 6):
    for x in range(0, i):
        z += 1
        print(z, end=' ')
    print('\n')
'''
#EX-54
'''
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
numero = number()
veri = primo(numero)
if(veri == True):
    print(f"{numero} É primo!")
else:
    print(f"{numero} Não é primo!")
'''
#EX-55 && 56 && 57 && 58
'''
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
            print(z)
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
print(f"Soma de todos os primos até 2M {soma()}")
a = number()
b = number()
print(f"De A a B: {AandB(a, b)}\n Soma A and B:{somaAandB(a, b)}")
'''
#EX-59
'''
???????
'''
#EX-60
'''
#NUMBER
def number():
    numero = int(input("Digite: "))
    return numero
#SOMANUMBER
def soma(antigo, novo):
    antigo += novo
    return antigo
#MediaDosNumero
def media(quant, antigo):
    media = antigo / quant
    return media
#Maior
def maior(antigo, novo):
    if(novo > antigo):
        return novo
    else:
        return antigo
#Menor
def menor(antigo, novo):
    if(novo < antigo):
        return novo
    else:
        return antigo
#MEDIAPAR
def mediaPar(quantPar, somaPar):
    media = somaPar / quantPar
    return media
#Par
def par(number):
    if(number%2==0):
        return True
    else:
        return False
#SomaPar
def somaPar(antigoPar, novoPar):
    if(par(novoPar) == True):
        antigoPar += novoPar
    return antigoPar
#CodeHome
const = True
quant = 0
quantPar = 0
medias = 0
mediaPars = 0
maiors = 0
menors = 0
somas = 0
somaPars = 0
while(const == True):
    numero = number()
    if (numero == 0):
        const = False
    else:
        somas = soma(somas, numero)
        if(par(numero) == True):
            somaPars = somaPar(somaPars, numero)
            quantPar += 1
            mediaPars = mediaPar(quantPar, somaPars)
        maiors = maior(maiors, numero)
        if(menors == 0):
            menors = numero
        menors = menor(menors, numero)
        quant += 1
        medias = media(quant, somas)
print(f"(a) A soma dos número digitados {somas}\n(b) A quantidade de números digitados {quant}\n(c) A média dos números digitados {medias}\n(d) O maior número digitado {maiors}\n(e) O menor número digitado {menors}\n(f) A média dos número pares {mediaPars}")
'''
#EX-61