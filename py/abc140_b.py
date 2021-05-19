N = int(input())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))
lc = list(map(int, input().split()))

ans = 0
prev = -1
for a in la:
    ans += lb[a-1]
    if prev + 1 == a:
        ans += lc[prev-1]
    prev = a
print(ans)
