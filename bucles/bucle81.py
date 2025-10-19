for n in range(2, 20):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n)
