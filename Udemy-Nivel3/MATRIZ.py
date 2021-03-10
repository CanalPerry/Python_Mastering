#Def Number
def numero(n, x):
    number = int(input(f"Coluna: {n + 1} Linha: {x + 1}\n Digite Número: "))
    return number

#CODEHOME
linha = int(input("Digite a Quantidade de Linha: "))
coluna = int(input("Digite a Quantidade de coluna: "))

matriz = [[numero(n, x) for n in range(0, coluna)]for x in range(0, linha)]
print("   This is Matriz: ")
[print(f"| {i} |")for i in matriz]