# 2 <= N <= 10**5
N = int(input())
la = [int(input()) for _ in range(N)]

cnt = 0
idx = 0
while cnt <= N:
    nextb = la[idx] - 1
    cnt += 1
    if nextb == 1:
        break
    idx = nextb

print(-1 if cnt > N else cnt)
