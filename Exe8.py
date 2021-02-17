'''

8 - Escreva um programa que leia 10 números e escreva o menor valor lido , eo maior valor lido.

'''
qtd = int(input("Digite: "))
c = 0
b = 0
x = 0
for i in range(1, qtd + 1):
    num = int(input("Digite: "))
    x = num
    if b == 0:
        c = x
        b = x
    elif x > c:
        c = x
    elif x < b:
        b = x
print(f"{c} é o maior numero, {b} é o menor numero. ")