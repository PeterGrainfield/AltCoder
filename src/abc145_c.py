# 2 <= N <= 8
import itertools
N = int(input())
lxy = []
ldis = []
for i in range(N):
    lxy.append(list(map(int, input().split())))

for lst in itertools.permutations(lxy):
    dis = 0
    for i in range(1, len(lst)):
        dis += ((lst[i][0] - lst[i-1][0])**2 +
                (lst[i][1] - lst[i-1][1])**2)**0.5

    ldis.append(dis)

ave = sum(ldis) / len(ldis)

print("{:.10f}".format(ave))
