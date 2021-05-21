X, N = map(int, input().split())
lp = set(map(int, input().split()))

for i in range(100):
    if X-i not in lp:
        print(X-i)
        exit()
    elif X+i not in lp:
        print(X+i)
        exit()
