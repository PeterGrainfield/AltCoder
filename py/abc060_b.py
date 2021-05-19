A, B, C = map(int, input().split())
ans = False
for i in range(A, A*B+1, A):
    if i % B == C:
        ans = True
        break

print("YES" if ans else "NO")
