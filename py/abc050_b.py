N = int(input())
lt = list(map(int, input().split()))
M = int(input())
ld = []
for i in range(M):
    _lt = lt.copy()
    P, X = map(int, input().split())
    _lt[P-1] = X
    print(sum(_lt))
