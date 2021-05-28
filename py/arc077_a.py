from typing import Deque


n = int(input())
la = list(map(int, input().split()))

lb = Deque()
turn = True
for a in la:
    if turn:
        lb.append(a)
    else:
        lb.appendleft(a)
    turn = not turn

ans = []
if turn:
    ans = lb
else:
    ans = list(lb)[::-1]
print(*ans)
