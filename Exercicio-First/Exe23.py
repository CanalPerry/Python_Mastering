# 23.Faça um algoritmo que leia um número positivo e imprima seus divisores.

#divisores
def fat(x, y):
    if x % y == 0:
        return True
    else:
        return False
#CodeHome
divisores = []
num = int(input("Digite numero: "))
for i in range(1, num):
    if fat(num, i) == True:
        divisores.append(i)
print(f'Esses são os divisores: {divisores}')