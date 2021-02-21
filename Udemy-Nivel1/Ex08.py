'''8.Leia uma temperatura em graus Kelvin e apresente-a
convertida em graus Kelvin. A fórmula de conversão é: C = K + 273.15,
snedo C a temperatura em Celsius e K a temperatura em Kelvin'''
K = float(input("Digite a temperatura em Kelvin: "))
C = K - 273.15
print(f"{K:.1f}°K transformado em Celsius: {C:.1f}°C")