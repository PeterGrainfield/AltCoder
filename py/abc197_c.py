import math
R, X, Y = map(int, input().split())

d = (X**2 + Y**2) ** 0.5
if d < 2 * R and d != R:
    ans = 2
else:
    ans = math.ceil(d/R)
print(ans)
