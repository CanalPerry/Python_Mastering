# 1.Faça um programa que recebe um um lista de tamanho 100 e coloca o indice no lugar do número par

list = [n for n in range(1, 100)]
for i in range(0, len(list)):
    if i % 2 == 0:
        list[i] = i
print(list)