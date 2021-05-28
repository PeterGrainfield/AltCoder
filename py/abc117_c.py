N, M = map(int, input().split())
lx = list(map(int, input().split()))
lx.sort()
diff = []
for i in range(1, len(lx)):
    diff.append(lx[i]-lx[i-1])

diff.sort()
# print(diff)
if N == 1:
    cost = diff
else:
    cost = diff[0:-N+1]
print(sum(cost))
