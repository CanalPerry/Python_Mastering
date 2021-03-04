 # Faça um programa que lei um numero e faça a tabuada do 0 a 10
#CodeHome
while True:
   n1 = int(input("Digite: "))
   [print(f"{n1} x {x} = {n1 * x}")for x in range(1, 10+1)]
   op = input("Deseja sair:\n S / N\n Digite: ")
   if op == 'S':
       break
