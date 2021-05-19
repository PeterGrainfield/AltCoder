lab = [list(map(int, input().split())) for _ in range(3)]

road = [0]*4

for ab in lab:
    road[ab[0]-1] += 1
    road[ab[1]-1] += 1

if min(road) == 0:
    print("NO")
elif max(road) == 3:
    print("NO")
else:
    print("YES")
