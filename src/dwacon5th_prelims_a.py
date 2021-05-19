N = int(input())
la = list(map(int, input().split()))

aveA = sum(la) / N

minDiff = 101

ans = 0
for i,a in enumerate(la):
    if minDiff > abs(a-aveA):
        minDiff = abs(a-aveA)
        ans = i
print(ans)



