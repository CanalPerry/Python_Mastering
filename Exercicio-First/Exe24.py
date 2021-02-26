# 24.Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
# com exceção dele próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

#NUMBER
def number():
    numero = int(input("Digite um numero: "))
    return numero
#DIVISORES
def fat(x, y):
    if x % y == 0:
        return True
    else:
        return False
#CodeHome
divsors = []
num = number()
cont = 0
x = 1
for i in range(1, num):
    if(fat(num, i) == True):
        if i != num:
            divsors.append(i)
print(divsors)
for i in range(0, len(divsors)):
    cont += divsors[i]
print(cont)