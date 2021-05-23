r, g, b = map(str,input().split())

n = int(r+g+b)
if n % 4:
    print("NO")
else:
    print("YES")