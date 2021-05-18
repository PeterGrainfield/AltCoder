S = input()
ans = False
smallcaps = [chr(i) for i in range(ord('a'), ord('z') + 1)]
if S[0] == 'A':
    cnt = 0
    indc = 0
    for i, c in enumerate(S[2:-1]):
        if c == 'C':
            cnt += 1
            indc = i + 2
    if cnt == 1:
        lips = S[1:indc] + S[indc+1:]
        allSmall = True
        for c in lips:
            if c not in smallcaps:
                allSmall = False
            ans = allSmall
print("AC" if ans else "WA")
