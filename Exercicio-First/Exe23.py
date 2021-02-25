# 23.Faça um algoritmo que leia um número positivo e imprima seus divisores.

def fat(x, y): # Para saber se o resto será 0 assim o a divisão dara certo.
    if x % y == 0:
        return True
    else:
        return False
def remove(lista):# Para remover os numeros iguais da lista DIV
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
x = int(input("Digite: "))
y = 2
mult = []
D = []
b = 1
c = []
number = []
div = []
number.append(x)
div.append(x)
while x > 1:
    if fat(x, y):
        x = x / y
        c.append(x)
        mult.append(y)
    else:
        y = y + 1
for i in range(0, len(mult)):
    D.append(b)
    b = b * mult[i]
div = mult + D + c + div
print("O números divisores de ", number, " são: ", remove(div))