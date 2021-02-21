#Number
def number():
    numero = int(input("Digite um numero: "))
    return numero
#Matriz
def matriz(linha, coluna):
    origem = []
    fim = []
    for i in range(0, coluna):
        print(f"{i+1}° Linha.")
        for x in range(0, linha):
            num = number()
            origem.append(num)
        fim.append(origem)
        origem = []
    return fim
#CodeHome
print("Numero de Colunas: ")
coluna = number()
print("Numero de linhas: ")
linha = number()
matri = matriz(linha, coluna)
for i in range(0, linha):
    for v in range(0, coluna):
        print(f"| {matri[i][v]} |", end='')
    print("")