# Пример замыкания

def add_number(a):
    def add(b):
        return a + b

    return add


# декоратор
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("before")
            result = func(*args, **kwargs)
            for i in range(n):
                print(i)
            print("after")
            return result

        return wrapper

    return decorator


@repeat(2)
def some_decorator():
    print("Hello")
    return 1


if __name__ == '__main__':
    # add_five = add_number(5)
    # print(add_five(3))
    some_decorator()
