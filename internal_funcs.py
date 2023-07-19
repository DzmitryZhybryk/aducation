# map

"""
Map - это такая функция, которая может быть применена к коллекции.
Она применяет некоторую функцию к каждому элементу коллекции
"""

a = [i for i in range(4)]
b = map(lambda x: x ** 2, a)
print(list(b))

"""
Filter - это такая функция, которая применяет некоторую функцию к элементу последовательности и если функция, 
которая указана 0 аргументом True, то элемент остаётся в последовательность. Если False, то нет
"""

a = [i for i in range(4)]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

"""
Zip - это такая функция, которая сразу может пройтись по нескольким коллекциям
"""

a = [i for i in range(4)]
b = [i for i in range(11)]
c = [i for i in range(2)]

for i in zip(a, b, c):
    print(i)

"""
Max + lambda
"""

a = {1: 3, 2: 2, 3: 1}
result = max(a)  # найдет самый большой ключ
result1 = max(a, key=lambda x: a[x])  # найдет самый большой value

"""
Reduce - функция, которая первым аргументом принимает в себя другую функцию (которая должна принимать в 
себя два аргумента), и вторым аргументом принимает последовательность элементов.
"""

from functools import reduce


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev + el


test = reduce(reducer_func, [1, 2, 3])  # 6
print(test)
