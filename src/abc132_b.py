n = int(input())
lp = list(map(int, input().split()))

ans = 0
for i in range(1, n-1):
    if lp[i-1] <= lp[i] and lp[i] <= lp[i+1]:
        ans += 1
    elif lp[i+1] <= lp[i] and lp[i] <= lp[i-1]:
        ans += 1
print(ans)
