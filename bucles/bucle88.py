a = [1, 2]
b = [3, 4]
for i in range(len(a)):
    a[i], b[i] = b[i], a[i]
print(a, b)
