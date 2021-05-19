N = int(input())
ld = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    if ld[i][0] == ld[i][1]:
        cnt += 1
        if cnt > 2:
            print("Yes")
            break
    else:
        cnt = 0
else:
    print("No")
