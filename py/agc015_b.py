S = input()

sts = len(S) - 1
ans = 0
for i, c in enumerate(S):
    if c == "D":
        ans += sts + sts - i
    else:
        ans += sts + i
print(ans)
