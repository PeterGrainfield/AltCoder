def cntDouble(str):
    n = 0
    i = 0
    while i < len(S)-1:
        c0 = S[i]
        c1 = S[i+1]
        if c0 == c1:
            n += 1
            i += 1
        i += 1
    return n


S = input()
K = int(input())

n1 = cntDouble(S)

ans = 0
if S[0] == S[-1]:
    a = 0
    for c in S:
        if c == S[0]:
            a += 1
        else:
            break
    b = 0
    for c in S[::-1]:
        if c == S[0]:
            b += 1
        else:
            break
    if a == len(S):
        ans = len(S) * K // 2
    else:
        ans = K*n1
        ans -= (a//2 + b//2 - (a+b)//2)*(K-1)
    print(ans)
else:
    print(K*n1)
