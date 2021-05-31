A, B = map(int, input().split())

ans = 0
A = A + 1 if A < 0 else A
B = B + 1 if B < 0 else B
print(B - A)