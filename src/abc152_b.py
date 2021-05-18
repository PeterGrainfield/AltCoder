a, b = map(int, input().split())

sa = str(a)*b
sb = str(b)*a

if a <= b:
    print(sa)
else:
    print(sb)
