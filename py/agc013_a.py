N = int(input())
la = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

mode = la[1] - la[0]
div = 0

for i in range(1, N):
    # print(la[i-1])
    dif = la[i] - la[i-1]
    if mode != 0:
        if mode < 0 and dif > 0:
            # print("--")
            div += 1
            mode = 0
        elif mode > 0 and dif < 0:
            # print("--")
            div += 1
            mode = 0
    else:
        mode = dif


print(div+1)
