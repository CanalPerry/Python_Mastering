# EX-25

#CodigoPrincipal
max = 0
for i in range(1000, -1, -1):
    if(i % 3 == 0 and i % 5 == 0):
        max += i
print(max)