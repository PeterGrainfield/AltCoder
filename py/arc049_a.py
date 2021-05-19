S = input()
la = list(map(int, input().split()))

ans = ''
for i in range(len(S)):
    if i in la:
        ans += '"'
    ans += S[i]
else:
    if i+1 in la:
        ans += '"'
print(ans)