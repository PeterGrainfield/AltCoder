N, X = map(int, input().split())
lvp = [list(map(int, input().split())) for _ in range(N)]

alc = 0
for i, vp in enumerate(lvp):
    v, p = vp[0], vp[1]
    alc += v * p
    if alc > X * 100:
        print(i+1)
        break
else:
    print(-1)
