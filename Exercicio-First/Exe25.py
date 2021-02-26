# 25.Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

some = []
verdade = 0
for i in range(1, 1000):
    if i % 3 == 0:
        verdade = verdade + i
print(verdade)