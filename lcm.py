a, b = input().split()

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(a, b):
   lcm = (a*b)//gcd(a,b)
   return lcm

print(lcm(int(a), int(b)))