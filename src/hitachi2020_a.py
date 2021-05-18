S = input()

ans = True
if len(S) > 1:
    for i in range(0, len(S), 2):
        if S[i:i+2] != 'hi':
            ans = False
else:
    ans = False

print("Yes" if ans else "No")
