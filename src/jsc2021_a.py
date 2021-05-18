import math
X, Y, Z = map(int, input().split())

p = math.ceil(Y / X * Z - 1)

print(p)
