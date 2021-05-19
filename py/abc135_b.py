N = int(input())
lp = list(map(int,input().split()))

diff = 0
for i in range(1,N+1):
    if i != lp[i-1]:
        diff +=1
        if diff > 2:
            print("NO")
            break
else:
    print("YES")
