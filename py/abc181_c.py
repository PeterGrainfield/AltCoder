import itertools
N = int(input())
lxy = [list(map(int, input().split())) for _ in range(N)]

ans = False
for lxy in itertools.combinations(lxy, r=3):
    x1, y1 = lxy[0][0], lxy[0][1]
    x2, y2 = lxy[1][0], lxy[1][1]
    x3, y3 = lxy[2][0], lxy[2][1]
    dx = x1-x2
    dy = y1-y2

    if dx * (y3 - y1) == dy * (x3-x1):
        ans = True
        break

print("Yes" if ans else "No")
