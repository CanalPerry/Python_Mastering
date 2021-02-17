'''
6 - Faça um programa que leia 10 inteiros e imprima sua media.
'''
qtd = int(input("Digite a quantidade: "))
n = 0
for i in range(1, qtd+1):
    num = int(input("Digite: "))
    n = n + num
print(n/qtd)