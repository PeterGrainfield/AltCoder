N, K = map(int, input().split())
listT = [int(input()) for _ in range(N)]

ans = -1
for i in range(2, N):
    sumSleep = listT[i] + listT[i-1] + listT[i-2]
    if sumSleep < K:
        ans = i + 1
        break
print(ans)
