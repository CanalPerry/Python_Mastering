#Number
def number(x, y):
    numero = int(input(f"Coluna {x+1} | Linha {y+1} digite número: "))
    return numero
#CodeHome
print("--|Numero de Colunas|-- ")
coluna = int(input("Digite: "))
print("--|Numero de linhas|-- ")
linha = int(input("Digite: "))
#matri = matriz(coluna, linha)
matri = [[number(n, v) for n in range(0, coluna)]for v in range(0, linha)]
for i in range(0, linha):
    for v in range(0, coluna):
        print(f"| {matri[i][v]} |", end='')
    print("")