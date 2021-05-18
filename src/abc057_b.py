N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
lcd = [list(map(int, input().split())) for _ in range(M)]

for ab in lab:
    distance = 10**9
    cpoint = 0
    for i, cd in enumerate(lcd):
        if abs(ab[0]-cd[0]) + abs(ab[1]-cd[1]) < distance:
            distance = abs(ab[0]-cd[0]) + abs(ab[1]-cd[1])
            cpoint = i+1
    print(cpoint)
