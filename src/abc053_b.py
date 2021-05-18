S = input()

ia, iz = 0, 200000
for i, c in enumerate(S):
    if c == 'A':
        ia = i
        break
for i, c in enumerate(S[::-1]):
    if c == 'Z':
        iz = len(S) - i - 1
        break

ans = iz - ia + 1
print(ans)
