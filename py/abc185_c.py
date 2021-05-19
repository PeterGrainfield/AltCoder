import math
L = int(input())
n = L - 1
kf = math.factorial(11)
ans = math.factorial(n)//(kf*math.factorial(n-11))
print(ans)
