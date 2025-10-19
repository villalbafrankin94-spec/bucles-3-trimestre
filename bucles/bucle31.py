
datos = ["1", "dos", "3"]
for d in datos:
    try:
        print(int(d))
    except ValueError:
        print("No es número")
