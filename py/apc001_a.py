X, Y = map(int,input().split())

for i in range(1,X*Y+1):
    if (X*i)%Y:
        print(X*i)
        break
else:
    print(-1)