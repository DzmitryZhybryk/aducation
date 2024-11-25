# Через Рекурсию

def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n


print(fac(5))

# Через While

# n = int(input())
n = 5

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)

# Через For

# n = int(input())
n = 5

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)
