import math
N = int(input())

ans = [0]*N
m = math.ceil(N**0.5)
for i in range(1, m):
    for j in range(1, m):
        for k in range(1, m):
            f = i**2 + j**2 + k**2 + i*j + j*k + k*i
            if f <= N:
                ans[f-1] += 1
for n in range(N):
    print(ans[n])
