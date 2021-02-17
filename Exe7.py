'''

7 - Faça um programa leia 10 inteiros positivos,ignorando não positivos,e imprima sua media.

'''
qtd = int(input("Digitar: "))
n = 0
for i in range(1, qtd+1):
    num = int(input("Digite: "))
    if num > 0:
        n = num + n
print(n/qtd)
