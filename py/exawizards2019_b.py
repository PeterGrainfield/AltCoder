N = int(input())
s = input()

ans = 0
for c in s:
    if c == "R":
        ans += 1
    else:
        ans -= 1
print("Yes" if ans > 0 else "No")
