 # Faça um programa que lei um numero e faça a tabuada do 0 a 10

tab = []
n1 = int(input("Digite: "))
for i in range(0,10+1):
    x = n1 * i
    tab.append(x)
for i in range(0,10+1):
    print(n1,"X",i,"=",tab[i])