#FindDuplicateNumber
def find(lista):
    D = []
    for i in range(0, len(lista)):
        for v in range(0, len(lista)):
            if lista[i] == lista[v] and i != v:
                if verifik(D, lista[i]) == False or D == []:
                    D.append(lista[i])
    return D
#Verifique
def verifik(l, numb):
    cont = 0
    for i in range(0, len(l)):
        print(l)
        print(l[i], numb)
        if l[i] == numb:
            return True
        else:
            cont += 1
    if cont != 0:
        return False
#CodeHome
lista = [1,2,2,4,4,8,8,9,9]
print(find(lista))