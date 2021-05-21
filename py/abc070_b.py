A, B, C, D = map(int,input().split())

t = min(B,D) - max(A,C)

if t <= 0:
    print(0)
else:
    print(t)