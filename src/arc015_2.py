N = int(input())

ans = [0]*6
for i in range(N):
    maxT, minT = map(float, input().split())
    if maxT >= 35:
        ans[0] += 1
    elif maxT >= 30:
        ans[1] += 1
    elif maxT >= 25:
        ans[2] += 1
    
    if minT >= 25:
        ans[3] += 1
    
    if maxT < 0:
        ans[5] += 1
    elif minT < 0:
        ans[4] += 1
print(*ans)
