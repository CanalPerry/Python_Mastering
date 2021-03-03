pessoa = ['arthur', 'nicolas', 'maria']
print([amigo.title() for amigo in pessoa])
numero = [1, 2, 3, 4, 5, 6]
print(f"Numeros pares: {[n for n in numero if not n % 2]}")
print(f"Numeros impares: {[n for n in numero if n % 2]}")
print(f"Numeros dividos: {[n / 2 for n in numero]}")
print(f"Numeros Multiplicado: {[n * 2 for n in numero]}")
print(f"Numeros de 0 a 100:{[n for n in range(0, 100+1)]}")
numb = [n for n in range(0, 100+1)]
linha = 3
coluna = 3

tabuleiro = [[int(input(f"Coluna {n+1} e Linha {v+1}: ")) for n in range(0, coluna)]for v in range(0, linha)]
print(tabuleiro)
[print(f"|{valor}|")for valor in tabuleiro]
