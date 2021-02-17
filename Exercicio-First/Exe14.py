'''

14- Faça um programa que leia um número inteiro positivo N par e imprima todos os números pares de 0 até N em ordem
decrescente.

'''
n = int(input("Digite: "))
for i in range(0, n + 1):
    if n % 2 == 0:
        print(n)
    n -= 1