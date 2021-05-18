N = int(input())
la = list(map(int,input().split()))

ans = 1
if 0 in la:
    ans = 0
else:
    for a in la:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
print(ans)
