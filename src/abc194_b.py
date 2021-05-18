N = int(input())
lab = [list(map(int, input().split())) for _ in range(N)]

lab = sorted(lab, key=lambda x: (x[0], x[1]))
alone = 10**5*2
ans = 10**5

for i in range(len(lab)):
    for j in range(len(lab)):
        if i == j:
            alone = min(alone, lab[i][0]+lab[i][1])
        else:
            ans = min(ans, max(lab[i][0], lab[j][1]))

ans = min(ans, alone)
print(ans)
