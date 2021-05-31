N, M = map(int, input().split())

ans = 0

if 2*N >= M:
    ans = min(N,M//2)
else:
    ans = N + (M-2*N)//4

print(ans)