def first():
    yield 1
    yield 1


def second():
    yield from first()
    yield 2
    yield 2


if __name__ == '__main__':
    test = second()
    for i in test:
        print(i)