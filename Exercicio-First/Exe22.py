# 22.Escreva um programa completo que permite a qualquer aluno introduzir,pelo teclado,
# uma sequência arbitrária de notas(válidas no intervalo de 10 a 20)e que mostre na tela,
# como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar
# o cálculo não será fornecido ao programa, o qual terminará quando for introduzido um valor que não
# seja válido como nota de aprovação.

def val(x):
    if x >= 10 and x <= 20:
        return True
    else:
        return False


m = True
list = []
b = 0
v = 0
p = 0
while m == True:
    print("Print um número entre 10 e 20,e para termina o programa digite um numero fora.")
    p = int(input("Digite: "))
    if val(p) == True:
        list.append(p)
        m = True
    else:
        m = False
for i in range(0, len(list)):
    b = i + list[i]
m = len(list)
v = b / m
print(v)

cro1 = []
cro2 = []
dd =[]
d = int(input("Digite: "))
cro1.append(d)
m = int(input("Digite: "))
cro1.append(m)
a = int(input("Digite:"))
cro1.append(a)
print(cro1)
d = int(input("digite: "))
cro2.append(d)
m = int(input("digite: "))
cro2.append(m)
a = int(input("digite: "))
cro2.append(a)
for i in range(0, 3):
    if cro1[i] > cro2[i]:
        dd = list(cro1)
    else:
        dd = list(cro2)
print(dd)