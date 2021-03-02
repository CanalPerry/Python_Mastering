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
        if l[i] == numb:
            return True
        else:
            cont += 1
    if cont != 0:
        return False
#CodeHome
lista = [2,3,2,3,5,5,0,0]
mostra = find(lista)
print(f"Número duplicados da lista {lista} : ")
for i in range(0, len(mostra)):
    print(f"| {mostra[i]} |", end="")