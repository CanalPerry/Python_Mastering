#EX-53

#NUMBER
def number():
    numero = int(input("Digite: "))
    return numero
#CODEHOME
z = 0
v = 0
for i in range(1, 6):
    for x in range(0, i):
        z += 1
        print(z, end=' ')
    print('\n')