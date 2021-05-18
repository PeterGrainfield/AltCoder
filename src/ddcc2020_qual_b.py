# 2≤N≤200000
N = int(input())
la = list(map(int, input().split()))

sumla = sum(la)
mdif = sumla

cnt = 0
for i in range(N):
    cnt += la[i]
    dif = abs(sumla - 2 * cnt)
    mdif = min(mdif, dif)

print(mdif)
