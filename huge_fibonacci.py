def pisanoPeriod(m):
    a, b = 0, 1
    for i in range(0, m*m):
        a, b = b, (a + b) % m
        if (a == 0 and b == 1):
            return i + 1

def fibonacci(n, m):
    pisano_period = pisanoPeriod(m)
    n = n % pisano_period

    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(n-1):
        a, b = b, a + b

    return b % m

n, m = input().split()
print(fibonacci(int(n), int(m)))