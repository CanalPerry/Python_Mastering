'''7.Leia uma temperatura em graus Fahrenheit e apresente-a em
graus Celsius. A fórmula de conversão é: C = 5.0*(F - 32.0)/9.0, sendo
C a temperatura em Celsius e F a temperatura em Fahrenheit.'''
F = float(input("Digite a temperatura Fahrenheit: "))
C = 5.0*(F - 32.0) / 9.0
print(f"{F:.1f}°F transformado em celsius é: {C:.1f}°C")