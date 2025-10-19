cadena = "Hola mundo"
contador = {}
for c in cadena:
    contador[c] = contador.get(c, 0) + 1
print(contador)