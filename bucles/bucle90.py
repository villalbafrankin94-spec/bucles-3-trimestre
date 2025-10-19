
class Contador:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration

for x in Contador(3):
    print(x)
