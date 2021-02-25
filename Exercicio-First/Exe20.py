# 20. ler uma sequência de números inteiros e determinar se eles são pares ou não.Deverá ser informado
# o número de dados lidos e número de valores pares.
# O processo termina quando for digitado o número 1000.

list = []
dados=[]
for i in range(0, 1000):
    dados.append(i)
    if i % 2 == 0:
        list.append(i)
print(len(list))
print(len(dados))