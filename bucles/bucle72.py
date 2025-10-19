texto = ""
with open("texto.txt") as f:
     for linea in f:
         texto += linea.strip() + " "
print(texto)