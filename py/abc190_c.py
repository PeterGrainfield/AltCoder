import itertools

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
lcd = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for comb in itertools.product((True, False), repeat=K):
    balls = [False]*N
    for i, cd in enumerate(lcd):
        t = cd[0]-1 if comb[i] else cd[1]-1
        balls[t] = True
        cond = 0
        for ab in lab:
            if balls[ab[0]-1] and balls[ab[1]-1]:
                cond += 1
        ans = max(ans, cond)

print(ans)
