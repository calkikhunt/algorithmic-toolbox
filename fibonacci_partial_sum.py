from cmath import pi


def fibonacci(n, m):
    assert not n > m

    x = [0, 1]
    pisano_period = 60
    for i in range(pisano_period - 2):
        x.append((x[-1] + x[-2]) % 10)
    
    n = n % pisano_period
    m = m % pisano_period
    if m < n:
        m = m + pisano_period

    res = 0
    for i in range(n, m + 1):
        res = res + (x[i % pisano_period])

    return res % 10

n, m = input().split()
print(fibonacci(int(n), int(m)))

# http://thisthread.blogspot.com/2018/02/last-digit-of-sum-of-fibonacci-numbers.html