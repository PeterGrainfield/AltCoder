S = input()
T = input()

ans = False
for i in range(len(S)):
    S = S[-1] + S[:-1]
    if S == T:
        ans = True
        break
print("Yes" if ans else "No")
