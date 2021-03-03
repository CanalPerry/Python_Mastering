#Como você encontra todos os pares de uma matriz inteiro cuja soma é igual a um determinado número?
#SomaPar
def SumPairs(lista):
    comb = []
    for x in range(0, len(lista)):
        for y in range(0, len(lista)):
            for z in range(0, len(lista)):
                for w in range(0, len(lista)):
                    if lista[x] + lista[y] == lista[z] + lista[w] and lista[x] != lista[z] and lista[x] != lista[w] and lista[y] != lista[w] and lista[y] != lista[z]:
                        if (lista[x] % 2) + (lista[y] % 2) + (lista[z] % 2) + (lista[w] % 2) == 0:
                            if lista[x] != lista[y] and lista[z] != lista[w]:
                                comb.append(f"{lista[x]} + {lista[y]} = {lista[z]} + {lista[w]} = {lista[x] + lista[y]}")
    return comb
#CodeHome
lista = []
numb = int(input("Digite numero: "))
for i in range(1, numb+1):
    lista.append(i)
sum = SumPairs(lista)
for i in range(0, len(sum)):
    print(f"| {sum[i]} |")