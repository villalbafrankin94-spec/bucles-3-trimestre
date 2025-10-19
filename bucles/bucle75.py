
def generador_cuadrados(n):
    for i in range(n):
        yield i**2

for x in generador_cuadrados(5):
    print(x)
