def fibonacci(n):
    x = [0, 1]
    if n in x:
        return n
    a, b = x
    for i in range(n-1):
        a, b = b, (a + b) % 10
    return b

n = int(input())
print(fibonacci(n))