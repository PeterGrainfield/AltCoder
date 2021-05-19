N, X = map(int, input().split())
listL = list(map(int, input().split()))

d = 0
bound = 1
for L in listL:
    d = d + L
    if d > X:
        print(bound)
        break
    bound += 1
else:
    print(N+1)