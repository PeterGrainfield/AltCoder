X, Y = map(int, input().split())

if Y % X == 0 or Y % X == X:
    print(-1)
else:
    print(X)
