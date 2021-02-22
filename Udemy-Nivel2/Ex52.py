# EX-52

# Aproximação
def aproxi(nota, saque):
    ghost = []
    true = []
    for i in range(0, len(nota)):
        r = saque - nota[i]
        ghost.append(r)
    for i in range(0, len(ghost)):
        if (ghost[i] <= saque and ghost[i] >= 0):
            true.append(nota[i])
    return true
#Contagem
def contagem(contag, saque, estrutura):
    const = True
    nota = 0
    lista = []
    contag = contag[::-1]
    print(contag)
    x = 0
    b = 0
    for i in range(0, len(contag)):
        if(estrutura >= contag[i]):
            while(const == True):
                if(contag[i] <= saque):
                    estrutura = estrutura - contag[i]
                    if(estrutura < contag[i] and not estrutura == contag[i]):
                        const = False
                nota += 1
                x += 1
            if(x > b):
                lista.append(f"Foram {nota} nota de {contag[i]}")
                b += 1
            if(estrutura == 0):
                break
            else:
                const = True
            nota = 0
    return lista
#Number
def number():
    numero = int(input("Digite: "))
    return numero
#CODEHOME
nota = [1, 2, 5, 10, 20, 50, 100]
saque = number()
contag = aproxi(nota, saque)
r = contagem(contag, saque, saque)
print(r)