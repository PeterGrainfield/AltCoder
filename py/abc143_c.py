N = int(input())
S = input()

prev = ""
ans = 0
for c in S:
    if c != prev:
        prev = c
        ans += 1

print(ans)