
with open("texto.txt") as f:
     total = 0
     for linea in f:
         total += len(linea.split())
print("Palabras:", total)
