# Faça uma função que recebe quatro números e ache a media aritimetica
def ari(x, y, z, t):
    total = x + y + z + t
    ari = total / 4
    return ari
n1 = int(input("Digite: "))
n2 = int(input("Digite: "))
n3 = int(input("Digite: "))
n4 = int(input("Digite: "))
print(ari(n1, n2, n3, n4))
