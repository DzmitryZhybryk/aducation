class Counter:
    current: int

    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        current += 1
        return current


c = Counter()
i = iter(c)
print(next(i))