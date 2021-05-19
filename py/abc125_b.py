N = int(input())
lv = list(map(int, input().split()))
lc = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += max(0, lv[i]-lc[i])
print(ans)
