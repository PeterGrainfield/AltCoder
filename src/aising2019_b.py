N = int(input())
A, B = map(int, input().split())
lp = list(map(int, input().split()))

diffCnt = [0]*3
for p in lp:
    if p > B:
        diffCnt[2] += 1
    elif p > A:
        diffCnt[1] += 1
    else:
        diffCnt[0] += 1

print(min(diffCnt))

