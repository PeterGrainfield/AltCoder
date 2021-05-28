from typing import Deque


def trimList(lh):
    for i in range(len(lh)):
        if lh[0] == 0:
            lh.popleft()
        else:
            break
    for i in range(len(lh)):
        if lh[-1] == 0:
            lh.pop()
        else:
            break
    lh.append(0)


N = int(input())
lh = Deque(list(map(int, input().split())))

ans = 0
trimList(lh)
while lh[0]:
    right = lh.index(0)
    for j in range(right):
        lh[j] -= 1
    ans += 1
    trimList(lh)

print(ans)
