N = int(input())
lxy = [list(map(int, input().split())) for _ in range(N)]

lxy.sort(key=lambda x: x[0])
lxyMinMax = []
lxyMinMax.append(lxy[0])
lxyMinMax.append(lxy[1])
lxyMinMax.append(lxy[-1])
lxyMinMax.append(lxy[-2])
lxy.sort(key=lambda x: x[1])
lxyMinMax.append(lxy[0])
lxyMinMax.append(lxy[1])
lxyMinMax.append(lxy[-1])
lxyMinMax.append(lxy[-2])
lxyCandidate = []
for xy in lxy:
    if xy in lxyMinMax:
        lxyCandidate.append(xy)
# print(lxyCandidate)
lxy = lxyCandidate

distance = []
for i in range(len(lxy)):
    h1x, h1y = lxy[i][0], lxy[i][1]
    for j in range(i+1, len(lxy)):
        h2x, h2y = lxy[j][0], lxy[j][1]
        distance.append(max(abs(h1x-h2x), abs(h1y-h2y)))

distance.sort(reverse=True)
# print(distance, len(distance))
print(distance[1])
