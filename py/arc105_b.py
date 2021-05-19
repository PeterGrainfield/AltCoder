import math
from functools import reduce


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


N = int(input())
la = list(map(int, input().split()))


las = list(set(la))
ans = my_gcd(*las)

print(ans)
