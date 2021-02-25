# 19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saida cada um dos
# algarismos que compõem o número.

vdd = False
while vdd == False:
    n = int(input('Digite: '))
    if n >= 100 and n<= 999:
        vdd = True
    else:
        vdd = False
x = (n // 100)*100
y = ((n % 100)//10)*10
z = n % 10
print(x,y,z)