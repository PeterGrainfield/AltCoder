S = input()

S = S[0:-1]

ansS = ''
for i in range(1, len(S)//2 + 1):
    sliS = S[:i*2]
    dblS = S[:i]*2
    if sliS == dblS:
        ansS = sliS

print(len(ansS))
