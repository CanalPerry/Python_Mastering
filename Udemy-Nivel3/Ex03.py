# Faça um programa  que recebe dois números e digite o números entre eles

n1 = int(input("Digite: "))
n2 = int(input("Digite: "))
if n1 > n2:
    for i in range(n2, n1+1):
        i += 1
        print(i)
for i in range(n1, n2+1):
    i += 1
    print(i)