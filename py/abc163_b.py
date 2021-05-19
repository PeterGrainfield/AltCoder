N, M = map(int, input().split())
la = list(map(int, input().split()))

workload = sum(la)
if N < workload:
    print(-1)
else:
    print(N-workload)
