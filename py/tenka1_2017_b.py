N = int(input())
lab = [list(map(int, input().split())) for _ in range(N)]

maxAB = [0, 0]

for a, b in lab:
    if maxAB[0] < a:
        maxAB = [a, b]

print(maxAB[0]+maxAB[1])
