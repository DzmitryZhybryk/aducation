a = 1


def outer():
    b = 1

    def inner():
        global a
        a = 2

        nonlocal b
        b = 2

    inner()

    print(a, b)


if __name__ == '__main__':
    outer()
