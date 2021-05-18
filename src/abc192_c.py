N, K = map(int, input().split())

N = list(map(int, str(N)))
a = N
for i in range(K):
    g1 = sorted(a, reverse=True)
    g2 = sorted(a)
    n1, n2 = 0, 0
    for dig in g1:
        n1 += dig
        n1 *= 10
    n1 = n1//10
    for dig in g2:
        n2 += dig
        n2 *= 10
    n2 = n2//10

    a = list(map(int, str(n1-n2)))

ans = 0
for dig in a:
    ans += dig
    ans *= 10
ans = ans // 10
print(ans)
