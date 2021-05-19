S = input()

ans = True
cap = False
for c in S:
    if cap ^ c.isupper():
        ans = False
        break
    cap = not cap
print("Yes" if ans else "No")
