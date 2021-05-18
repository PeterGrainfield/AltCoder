lx = list(map(int, input().split()))

for i in range(len(lx)):
    if lx[i] == 0:
        print(i+1)
        break

