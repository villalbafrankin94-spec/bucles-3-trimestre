texto = "Python es divertido"
sin_vocales = "".join([c for c in texto if c.lower() not in "aeiou"])
print(sin_vocales)
