N = int(input())
T, A = map(int, input().split())
lh = list(map(int, input().split()))

target = T - A
dif = 10**5
ans = -1
for i in range(N):
    d = lh[i] * 0.006
    # print(i, d, target)
    if abs(target - d) < dif:
        dif = abs(target - d)
        ans = i + 1
print(ans)
