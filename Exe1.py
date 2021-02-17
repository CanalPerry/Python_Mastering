'''
1. Faça um programa que determine os cinco primeiros numeros multiplos de 3 , considaderando
que sejam maior que zero.
'''
for i in range(1, 16):
    n = i
    if n % 3 == 0:
        print(n)
