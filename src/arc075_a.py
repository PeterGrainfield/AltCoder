N = int(input())
ls = [int(input()) for _ in range(N)]

maxScore = sum(ls)
ans = 0
for s in ls:
    score = maxScore - s
    if score % 10 != 0:
        ans = max(ans, score)

if maxScore % 10 != 0:
    ans = maxScore
print(ans)
