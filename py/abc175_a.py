S = input()

ans = 0
cnt = 0
for c in S:
    if c == "S":
        cnt = 0
    else:
        cnt += 1
        ans = max(ans, cnt)

print(ans)
