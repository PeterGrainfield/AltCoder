A, B, C = map(int, input().split())

ans = ""
if A+B == C:
    ans += "+"
if A-B == C:
    ans += "-"

if ans == "+-":
    ans = "?"

print(ans if ans != '' else "!")
