N, M = map(int, input().split())
la = list(map(int, input().split()))

s = sum(la)
cnt = 0
for a in la:
    if 4 * M * a >= s:
        cnt += 1
        if cnt >= M:
            print("Yes")
            break
else:
    print("No")
