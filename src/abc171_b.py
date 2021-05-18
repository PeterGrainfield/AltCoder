N, K = map(int, input().split())
lp = list(map(int, input().split()))
lp.sort()

print(sum(lp[0:K]))
