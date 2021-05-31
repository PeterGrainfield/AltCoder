Y = int(input())

ans = False
if Y%4==0:
    if Y%100==0:
        if Y%400==0:
            ans = True
        else:
            ans = False
    else:
        ans =True
else:
    ans = False
print("YES" if ans else "NO")