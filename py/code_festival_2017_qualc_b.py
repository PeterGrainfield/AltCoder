# 1 <= N <= 10, 1 <= A <= 100
import itertools
N = int(input())

lspare = list(map(int, input().split()))

ld = (-1, 0, 1)

ans = 0
for ldif in itertools.product(ld, repeat=N):
    for i in range(N):
        n = lspare[i] + ldif[i]
        if n % 2 == 0:
            ans += 1
            break
print(ans)
