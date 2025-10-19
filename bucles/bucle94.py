
original = [1, 2, 2, 3, 3, 3]
sin_duplicados = []
for x in original:
    if x not in sin_duplicados:
        sin_duplicados.append(x)
print(sin_duplicados)
