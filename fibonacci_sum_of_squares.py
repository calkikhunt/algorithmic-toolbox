def fibonacci(n):
    f = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        f.append(f[i-1] + f[i-2])
        last.append(f[i] % 10)

    x = last[n % 60] * last[n % 60] + last[n % 60] * last[(n - 1) % 60]
    return x % 10

n = int(input())
print(fibonacci(n))