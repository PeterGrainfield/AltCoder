N = int(input())
listLR = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for left,right in listLR:
    ans += right-left+1 
print(ans)