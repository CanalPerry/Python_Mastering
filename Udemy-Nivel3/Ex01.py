# 1.Faça um programa que recebe um um lista de tamanho 100 e coloca o indice no lugar do número par

list = []
for i in range(0,10+1):
    n1 = int(input("Digite: "))
    list.append(n1)
print(list)
for i in range(0, len(list)):
    if i % 2 == 0:
        list[i] = i
print(list)