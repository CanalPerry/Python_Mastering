'''

16 -Faça um programa que leia um número inteiro positivo impar N imprima todos os numeros impares 1 ate N
em ordem DEcrescente.

'''
n = int(input("Digite: "))
for i in range(0, n + 1):
    if n % 2 == 1:
        print(n)
    n -= 1