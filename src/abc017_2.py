S = list(input())

choku = ("o", "k", "u")

ans = True
while len(S) > 0:
    if len(S) >= 2 and S[-2:] == ["c", "h"]:
        S.pop()
        S.pop()
    elif S[-1] in choku:
        S.pop()
    else:
        ans = False
        break
print("YES" if ans else "NO")
