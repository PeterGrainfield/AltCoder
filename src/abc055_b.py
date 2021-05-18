# 1 <= N <= 10**5
import math
N = int(input())

ans = math.factorial(N)
# for i in range(1, N+1):
#     ans = ans*i
print(ans % (10**9+7))
