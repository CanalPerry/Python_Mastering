#11.Faça um programa que imprima a tabuada de 1 a 9
tabuada = [[print("|-----------|") if y == 11 else print(f"|{x} x {y} = {x * y}|")for y in range(1, 12)]for x in range(1, 10)]