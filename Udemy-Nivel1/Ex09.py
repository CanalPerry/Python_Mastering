'''
9.Leia uma temperatura em Graus Celsius e apresente-a convertida
em graus Kelvin. A fórmula de conversão é: K = C + 273.15, sendo
C a temperatura em Celsius e K a temperatura em Kelvin.
'''
C = float(input("Digite o graus celsius: "))
K = C + 273.15
print(f"{C:.1f}°C transformado em kelvin é: {K:.1f}°K")