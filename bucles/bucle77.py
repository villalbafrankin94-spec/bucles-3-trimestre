a = ["x", "y"]
b = [10, 20]
for i, (x, y) in enumerate(zip(a, b)):
    print(i, x, y)