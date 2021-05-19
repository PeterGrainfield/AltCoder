N = int(input())
la = list(map(int, input().split()))
r = [0]*9

for a in la:
    # monster
    if a >= 3200:
        r[8] += 1
        continue

    for i in range(8):
        if a < (i+1) * 400:
            r[i] += 1
            break

cnt = 0
rcnt = r[8]
for i in range(8):
    if r[i] > 0:
        cnt += 1

minCol = 0
if cnt > 0:
    minCol = cnt
else:  # cnt == 0
    minCol = 1

maxCol = cnt + rcnt
print(minCol, maxCol)
