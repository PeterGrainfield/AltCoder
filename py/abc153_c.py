N, K = map(int, input().split())
lh = list(map(int, input().split()))

lh.sort(reverse=True)

minAttack = sum(lh[min(K, len(lh)):])
print(minAttack)
