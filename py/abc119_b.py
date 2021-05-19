N = int(input())
lxu = [list(map(str,input().split())) for _ in range(N)]

ans = 0
for xu in lxu:
    if xu[1] == "BTC":
        ans += float(xu[0]) * 380000
    else:
        ans += int(xu[0])
print(ans)
