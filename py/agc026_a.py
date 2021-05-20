N = int(input())
la = list(map(int,input().split()))


pa = la[0]
ans = 0
for i in range(1,N):
    if pa == la[i]:
        pa = -1
        ans += 1
    else:
        pa = la[i]

print(ans)