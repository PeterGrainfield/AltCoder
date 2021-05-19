S = input()
K = int(input())

cnt = 0
for c in S:
    if c == '1':
        cnt += 1
    else:
        break

ans = ''
if K > cnt:
    ans = S[cnt]
else:
    ans = '1'

print(ans)
