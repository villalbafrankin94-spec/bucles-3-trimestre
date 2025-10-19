
contador = 0
with open("archivo.txt") as f:
     for _ in f:
         contador += 1
print("Líneas:", contador)
