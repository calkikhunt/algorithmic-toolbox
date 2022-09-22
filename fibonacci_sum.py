def fibonacci(n):
    if n <= 1:
        return n

    pisano_period = 60
    n = n % pisano_period

    x = [0, 1]
    for i in range(n + 1):
        x.append((x[-1] + x[-2]) % 10)

    return (x[-1] - 1) % 10

n = int(input())
print(fibonacci(n))