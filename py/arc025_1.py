ld = list(map(int, input().split()))
lj = list(map(int, input().split()))

ans = 0
for i in range(7):
    ans += max(ld[i], lj[i])

print(ans)