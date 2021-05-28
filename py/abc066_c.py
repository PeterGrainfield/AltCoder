from typing import Deque


n = int(input())
la = list(map(int,input().split()))

lb = Deque()
turn = True
for a in la:
    if turn:
        lb.append(a)
    else:
        lb.appendleft(a)

print(*lb if turn else *lb[::-1])