A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

D = abs(A-B)
dV = V-W

if dV <= 0:
    print("NO")
elif D <= dV * T:
    print("YES")
else:
    print("NO")
