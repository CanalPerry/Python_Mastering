'''
5- Faça um programa que peça para o usuario digitar 10 valores e some-os.
'''
qtd = int(input("Quantidade de vezes que esse numero deve roda. "))
i = 0
for n in range(1, qtd + 1):
    num = int(input("Digite: "))
    i = i + num
print(i)
