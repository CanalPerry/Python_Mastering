'''

9 - Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

'''
n = 0
inteiro = int(input("Digite um inteiro: "))
while n < inteiro:
    op = int(input("Digite: "))
    if op%2 == 1:
        print(op)
    n += 1