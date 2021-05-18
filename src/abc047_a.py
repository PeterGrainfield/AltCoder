a, b, c = map(int, input().split())

if max(a, b, c)*2 == sum([a, b, c]):
    print("Yes")
else:
    print("No")
