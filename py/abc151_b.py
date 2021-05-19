N, K, M = map(int, input().split())
la = list(map(int, input().split()))

needed = max(M*N - sum(la),0)

if needed > K:
    print(-1)
else:
    print(needed)
