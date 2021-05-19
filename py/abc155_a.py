A, B, C = map(int, input().split())

ans = False

if A == B and A != C:
    ans = True
elif A == C and A != B:
    ans = True
elif B == C and B != A:
    ans = True
print("Yes" if ans else "No")
