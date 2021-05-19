N = int(input())

ans = False
for i in range(1,10):
    d, r = divmod(N,i)
    if r==0 and d < 10:
        print("Yes")
        break
else:
    print("No")
