V, T, S, D = map(int, input().split())

ti = D / V
if ti < T or ti > S:
    print("Yes")
else:
    print("No")
