la = list(map(int, input().split()))

la.sort()

if la[2] - la[1] == la[1] - la[0]:
    print("Yes")
else:
    print("No")
