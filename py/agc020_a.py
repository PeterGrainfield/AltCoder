A, B, K = map(int, input().split())

factor = {0: 1}
for i in range(1, 60+1):
    factor[i] = factor[i-1]*i


def comb(a, b):
    comb = factor[a+b]//(factor[a]*factor[b])
    return comb


cnt = 0
ans = ""
for i in range(A+B):
    if A > 0:
        A -= 1
        com = comb(A, B)
        if com+cnt < K:
            A += 1
            cnt += com
            ans += "b"
            B -= 1
        else:
            ans += "a"
    else:
        B -= 1
        ans += "b"

print(ans)
