# EX-44

numero = 30
antigo = 0
novo = 1
resultado = 0
l1 = 0
l2 = 1
fibonnaci = []
fibonnaci.append(antigo)
fibonnaci.append(novo)
cont = True
while(cont == True):
    if(fibonnaci[l2] < numero):
        r = fibonnaci[l1] + fibonnaci[l2]
        fibonnaci.append(r)
        l1 += 1
        l2 += 1
    else:
        cont = False
print(fibonnaci)