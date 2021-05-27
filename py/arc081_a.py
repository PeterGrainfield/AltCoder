from typing import Counter


N = int(input())
la = list(map(int, input().split()))

counter = Counter(la)
sortedCnt = sorted(counter.items(), key=lambda x: x[0], reverse=True)

L = []
for length, cnt in sortedCnt:
    if cnt >= 4:
        L.append(length)
        L.append(length)
    elif cnt >= 2:
        L.append(length)
    if len(L) >= 2:
        print(L[0]*L[1])
        break
else:
    print(0)
