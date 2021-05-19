N, P = map(int, input().split())
la = list(map(int, input().split()))

cnt = [0]*2
for a in la:
    cnt[a % 2] += 1

ans = 0
if cnt[1] == 0:
    if P == 0:
        ans = 2**cnt[0]
else:
    ans = 2**(sum(cnt)-1)
print(ans)
