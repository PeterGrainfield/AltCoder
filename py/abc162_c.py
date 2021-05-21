import math
from functools import reduce


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


K = int(input())
ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        ab_gcd = math.gcd(a, b)
        for c in range(1, K+1):
            ans += math.gcd(ab_gcd, c)
print(ans)
