#6.Leia uma temperatura em graus CELSIUS e apresente-a
#convertida em graus Fahrenheit.
#A fórmula de conversão é: F = C *(9.0/5.0) + 32.0, sendo F
#a temperatura em Fahrenheit e C a temperatura em Celsius.
celsius = float(input("Digite o Celsius: "))
fahren = celsius *(9.0/5.0) + 32.0
print(f"{celsius}°C transformando em Fahrenheit. é {fahren}°F ")