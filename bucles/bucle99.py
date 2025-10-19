
texto = "programación"
vocales = "aeiouáéíóú"
indices = []
for i, letra in enumerate(texto):
    if letra.lower() in vocales:
        indices.append(i)
print(indices)
