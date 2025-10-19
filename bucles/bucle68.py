d = {"a": 1, "b": 2}
for v, k in [(v, k) for k, v in d.items()]:
    print(v, k)
