N = int(input())
la = list(map(int, input().split()))
numCnt = [0]*(10**5+1)
for a in la:
    if a != 0:
        numCnt[a-1] += 1
    numCnt[a] += 1
    numCnt[a+1] += 1
print(max(numCnt))
