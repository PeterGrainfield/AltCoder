import collections
N, K = map(int, input().split())
la = list(map(int, input().split()))

c = collections.Counter(la)

c_sorted = sorted(c.items(), key=lambda x: x[0])

remain = min(c_sorted[0][1], K)
prev = -1
ans = 0
for num, numCnt in c_sorted:
    if prev + 1 != num:
        break
    ans += remain - min(remain, numCnt)*(num)
    remain -= remain - min(remain, numCnt)
    prev = num
else:
    ans += remain*(prev+1)
print(ans)
