N = int(input())
lp = list(map(int, input().split()))
exists = [0]*200001
ans = 0
for p in lp:
    exists[p] = 1
    for i in range(ans, 200001):
        if exists[i] == 0:
            print(i)
            ans = i
            break
