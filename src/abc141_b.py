N = int(input())
la = list(map(int,input().split()))
lb = list(map(int,input().split()))
lc = list(map(int,input().split()))

ans = 0
prev = 0
for a in la:
    ans += lb[a]
    if prev + 1 == a:
        ans += lc[a]
    prev = a
print(ans)
