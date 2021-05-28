S = input()

ans = 0
for i in range(len(S)-1, 0, -1):
    c0 = S[i]
    c1 = S[i-1]
    n = 0
    if c1 in ("1234567890"):
        n = int(c1)
    if c0 in ("1234567890"):
        n = n*10+int(c0)

    ans = max(ans, n)
print(ans)
