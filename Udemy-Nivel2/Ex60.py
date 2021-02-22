#EX-60

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
