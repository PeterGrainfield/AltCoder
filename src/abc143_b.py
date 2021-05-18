N = int(input())
ld = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans += ld[i] * ld[j]

print(ans)
