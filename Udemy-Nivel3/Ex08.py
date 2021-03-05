musica = [{'titulo': 'Eu sou uma metamorfose ambulante', 'tocou': 2}, {'titulo': 'Azul da Cor do Mar', 'tocou': 3}]
print(max(musica, key=lambda music: music['tocou'])['titulo'])
print(min(musica, key=lambda music: music['tocou'])['titulo'])
print(round(10.246, 2))
soma = 3 + 2
print(soma)