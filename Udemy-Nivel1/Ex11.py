#11.Faça um programa que imprima a tabuada de 1 a 9
for i in range(1, 10):
    print("----------------")
    for v in range(1, 11):
        multi = i * v
        print(f"{i} x {v} = {multi}")
    print("----------------")