N = int(input())

tgt = list("indeednow")
tgt.sort()
for i in range(N):
    S = list(input())
    S.sort()
    if tgt == S:
        print("YES")
    else:
        print("NO")
