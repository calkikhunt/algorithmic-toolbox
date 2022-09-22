def gcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    number = gcd(b, a_prime)
    return number

n, m = input().split()
print(gcd(int(n), int(m)))