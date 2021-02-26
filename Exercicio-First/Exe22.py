# 22.Escreva um programa completo que permite a qualquer aluno introduzir,pelo teclado,
# uma sequência arbitrária de notas(válidas no intervalo de 10 a 20)e que mostre na tela,
# como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar
# o cálculo não será fornecido ao programa, o qual terminará quando for introduzido um valor que não
# seja válido como nota de aprovação.

#VERIFIK
def val(x):
    if x >= 10 and x <= 20:
        return True
    else:
        return False
#CODEHOME
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
tam = len(list)
v = b / tam
print(v)