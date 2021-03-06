#11.Faça um programa que imprima a tabuada de 1 a 9
tabuada = [[print("|-----------|") if y == 11 else print(f"|{x} x {y} = {x * y}|")for y in range(1, 12)]for x in range(1, 10)]
aluno = [{'Username': ''}]
aluno[0]['Username'] = input("Nome de Usuario: ")
print(aluno[0]['Username'])
x = lambda n: 3 + n ** 3
print(x(3))
v = 5
b = 2
if not v > b:
    maior = v
    print(maior)