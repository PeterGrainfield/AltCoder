import math
from functools import reduce


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


N = int(input())
nlist = list(range(2, N+1))
# print(nlist)
print(my_lcm(*nlist)+1)
