N, K = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
lab.sort(key=lambda x: x[0])
# print(lab)
m = K
i = 0
for a, b in lab:
    if a-i > m:
        i = i+m
        break
    else:
        m += b - (a-i)
        i = a
else:
    i = i+m

print(i)
