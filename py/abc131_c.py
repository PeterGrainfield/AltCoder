from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


A, B, C, D = map(int, input().split())

ans = 0
divC = B//C - (A-1)//C
divD = B//D - (A-1)//D
divCD = B//lcm(C, D) - (A-1)//lcm(C, D)

print((B-A+1)-(divC+divD-divCD))
