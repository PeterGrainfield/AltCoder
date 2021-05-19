S = input()
scrn = []
for i in range(len(S)):
    if S[i] == 'B':
        if len(scrn) > 0:
            scrn.pop()
    else:
        scrn.append(S[i])

print("".join(scrn))
