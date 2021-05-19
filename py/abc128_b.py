N = int(input())
lr = []
for i in range(N):
    S, P = map(str, input().split())
    lr.append([i, S, 100-int(P)])
slr = sorted(lr, key=lambda x: (x[1], x[2]))
for r in slr:
    print(r[0] + 1)
