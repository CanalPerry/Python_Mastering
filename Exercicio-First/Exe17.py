# 17 Faça um programa que leia um número inteiro  positivo N e calcule a soma dos n primeiros números
# naturais

list = []
x = 0
n = int(input("Digite: "))
for i in range(0, n+1):
    list.append(i)
for i in range(0, len(list)):
    x = x + list[i]
print(list)
print(x)