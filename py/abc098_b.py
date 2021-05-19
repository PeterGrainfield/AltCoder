N = int(input())
S = input()

ans = 0
for i in range(1, N):
    s1 = set(S[0:i])
    s2 = set(S[i:N])
    si = s1 & s2
    ans = max(ans, len(si))
print(ans)
