N = int(input())
la = list(map(int, input().split()))

ans = 0
cnt = 1
for a in la:
    if a == cnt:
        cnt += 1
    else:
        ans += 1

if cnt == 1:
    print(-1)
else:
    print(ans)
