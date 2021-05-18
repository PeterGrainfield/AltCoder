N = int(input())
ls = [list(input()) for _ in range(N)]
ls2 = []
for s in ls:
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    ls2.append(d)

# print(ls2)

ans = []
for c in range(ord("a"), ord("z") + 1):
    minCnt = 51
    for d in ls2:
        cnt = 0
        if chr(c) in d:
            cnt = d[chr(c)]
            minCnt = min(minCnt, cnt)
        else:
            minCnt = 0
    if minCnt > 0:
        ans.append(chr(c) * minCnt)

print("".join(ans))
