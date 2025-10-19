
texto = "banana"
frecuencia = {}
for letra in texto:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1

print(frecuencia)
