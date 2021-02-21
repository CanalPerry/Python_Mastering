'''
10. Leia uma velocidade em Km/h(quilômetros por hora) e apresente-a
convertida em m/s(metros por segundo). A fórmula de conversão é:
M = K/3.6, sendo K a velocidade em Km/ e M em m/s
'''
k = float(input("Digite a velocidade: "))
m = k/3.6
print(f"{k:.1f}km/h a velocidade transformada em m/s é: {m:.1f}m/s")