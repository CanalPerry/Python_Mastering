# 21. Faça um programa que Receba dois números. Calcule e mostre:
# - A soma dos números pares desse intervalo de números, incluindo os números digitados;
# - A multiplicação dos números ímpares desse intervalo, incluindo os digitados;

impar = []
x = 1
y = 0
par = []
n1 = int(input("Digite: "))
n2 = int(input("Digite: "))
if n1 < n2:
    for i in range(n1, n2+1):
        if i % 2 == 0:
            par.append(i)
        elif i % 2 == 1:
            impar.append(i)
elif n2 < n1:
    for i in range(n2, n1+1):
        if i % 2 == 0:
            par.append(i)
        elif i % 2 == 1:
            impar.append(i)
for i in range(1, len(impar)):
    x *= impar[i]
for i in range(0, len(par)):
    y += par[i]
print(impar, "IMPAR")
print(par, "PAR")
print(x, "IMPAR")
print(y, "PAR")