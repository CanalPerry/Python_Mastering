'''

10 - Faça um programa que calcula e mostra a soma dos 50 primeiros números pares.

'''
qtd = 50
x = 0
n = 0
for i in range(1, qtd + 1):
    num = int(input("Digite: "))
    if num%2 == 0:
        n = n + num
print(n)