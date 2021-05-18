X, Y = map(int,input().split())

if 2 * X <= Y and 4 * X >= Y and Y % 2 == 0:
    print("Yes")
else:
    print("No")