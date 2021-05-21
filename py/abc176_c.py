N = int(input())

la = list(map(int, input().split()))

maxHeight = 0
ans = 0
for a in la:
    if a > maxHeight:
        maxHeight = a
    else:
        ans += maxHeight - a
print(ans)