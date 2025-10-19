
with open("archivo.txt") as f:
     for linea in f:
         palabras = linea.split()
         for palabra in palabras:
          print(palabra)
