N = int(input())
lp = list(map(int, input().split()))

cnt = 1
jmin = lp[0]
for i in range(1, len(lp)):
    if jmin >= lp[i]:
        cnt += 1
        jmin = lp[i]
    else:
        if jmin == 1:
            break

print(cnt)
