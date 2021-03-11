with open('Tabuada.txt', 'w') as arq:
    arq.write('------ Tabuada:--------\n')
    for i in range(1, 11):
        for x in range(1, 11):
            arq.write(f'-- {i} x {x} = {i * x} ')
            arq.write('\n')
        arq.write('-----------------\n')

