# 18 Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas
# vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

def muda(b):
    if b == 0:
        return True
def maiob(x,b):
    if x < b:
        return True
def maion(x,n):
    if x < n:
        return True
cont = True
b = 0
qtd = 0
x = 0
s = 0
while cont == True:
    n = int(input("Digite o tamanho da lista: "))
    if muda(b) == True:
        b = n
        x = n
    elif maiob(x,b) == True:
        x = b
    elif maion(x,n) == True:
        x = n
        qtd += 1
    s = input("Desaja Sair . 'S' e 'N'?").upper()
    if s == 'S':
        cont = False
    else:
        cont = True
print(x)
print(qtd)