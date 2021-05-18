r, D, x2000 = map(int, input().split())

x = x2000
for i in range(2001,2011):
    x = r*x - D
    print(x)
