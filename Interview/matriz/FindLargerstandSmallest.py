#Como você encontra o maior e menor número em uma matriz inteiro não sortida?
#NumeroMaior
def maior(l):
    maior = 0
    for i in range(0, len(l)):
        if l[i] > maior:
            maior = l[i]
    return maior
#NumeroMenor
def menor(l):
    menor = None
    for i in range(0, len(l)):
        if (menor == None):
            menor = l[i]
        elif l[i] < menor and menor != None:
            menor = l[i]

    return menor

#CodeHome
lista = [30,5,10]
print(menor(lista))
print(maior(lista))