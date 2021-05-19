C = input()
ans = True
c0 = C[0]
for c in C:
    if c != c0:
        ans = False
print("Won" if ans else "Lost")
