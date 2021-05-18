from operator import itemgetter
K, N, M = map(int, input().split())
la = list(map(int, input().split()))

s, sp = divmod(M, N)

lb = []  # key 元の順番　value とりあえずの値
for i, a in enumerate(la):
    lb.append([i, a*s])

# ###
# print(lb)
# ###
lb.sort(key=itemgetter(1))

lbn = []
height = [0]*K
for i, bs in enumerate(lb):
    lbn.append(bs[1])
    if bs[1] == 0:
        height[i] = 10**9


# print(lbn)
print(height)
# 余りをどこに振り分けるか
# 一番低いところ、同じなら一番細かいもの

for i in range(sp):
    minH = min(height)
    for i in range(K):
        if height[i] == minH:
            height[i] += 1 / lbn[i]
            lb[i][1] += 1
            break

# lb.sort(key=itemgetter(0))
ans = [0]*K
for b in lb:
    ans[b[0]] = b[1]
print(*ans)
