with open('Capital.txt', 'w') as arq:
    number = int(input("Digite o CAPITAL: "))
    E = number * 0.02
    G = number * 0.05
    P = number * 0.02
    total = number
    cont = 0
    for i in range(1, 31):
        total = total + (total * 0.05)
        cont = i
    arq.write(f'Capital: {number}\n'
              f'Entrada ao dia: R$ {E:.2f}\n'
              f'Ganho ao dia: R$ {G:.2f}\n'
              f'Parada ao dia: R$ {P:.2f}\n'
              f'Juro Composto(30dias): {total:.2f}\n'
              f'Contagem de Dia: {cont}')