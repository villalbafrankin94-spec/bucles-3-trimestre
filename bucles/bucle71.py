with open("texto.txt") as f:
     for linea in f:
         if linea.strip() == "":
             print("Línea vacía")