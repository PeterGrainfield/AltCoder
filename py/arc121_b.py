from typing import Deque


N = int(input())
lac = [list(map(str, input().split())) for _ in range(2*N)]

lac.sort(key=lambda x: int(x[0]))
listR = Deque()
listG = Deque()
listB = Deque()

for a, c in lac:
    if c == "R":
        listR.append(int(a))
    elif c == "G":
        listG.append(int(a))
    else:
        listB.append(int(a))


def curPop(cl, cr, lis):
    if len(lis) > 1 and lis[0] == cl:
        lis.popleft()
        lis.popleft()
    if len(lis) > 1 and lis[0] == cr:
        lis.pop()
        lis.pop()


curL = int(lac[0][0])
curR = int(lac[-1][0])
while len(listR) + len(listG) + len(listB) > 4:
    curPop(curL, curR, listR)
    curPop(curL, curR, listG)
    curPop(curL, curR, listB)
    curL = 10**15+1
    curR = 0
    if len(listR) > 1:
        curL = min(curL, listR[0])
        curR = max(curR, listR[-1])
    if len(listG) > 1:
        curL = min(curL, listG[0])
        curR = max(curR, listG[-1])
    if len(listB) > 1:
        curL = min(curL, listB[0])
        curR = max(curR, listB[-1])

if len(listR) % 2 == 0 and len(listG) % 2 == 0 and len(listB) % 2 == 0:
    print(0)
else:
    li = list(listR+listG+listB)
    li.sort()
    if len(li) == 2:
        print(abs(li[0]-li[1]))
    elif len(li) == 4:
        print(min(abs(li[0]-li[1])+abs(li[2]-li[3]),
              abs(li[1]-li[2])+abs(li[0]-li[3])))
