#Como você encontra o número faltante em uma determinada matriz inteiro de 1 a 100?
import random
#RemoveItem
def remove(lista, x):
    del(lista[x+1])
    return lista
#MostrarLista
def mostra(lista):
    for i in range(0, len(lista)):
        print(f"| {lista[i]} |", end="")
        if lista[i] % 3 == 0:
            print("")
#NumeroRetirado
def retirado(lista):
    x = 1
    for i in range(0, len(lista)):
        if x != lista[i]:
            return x
            break
        else:
            x += 1
#CodeHome

num = int(input("Digite um numero: "))
lista = [n for n in range(1, num+1)]
print("LISTA COM TODOS OS NÚMEROS.")
mostra(lista)
choice = random.choice(lista)
lista = remove(lista, choice)
print("\n")
print("LISTA COM NÚMERO REMOVIDO.")
mostra(lista)
print("\n")
print(f"O numero faltante é: {retirado(lista)}")