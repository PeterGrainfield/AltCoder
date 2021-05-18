S = input()
ans = ""
for c in S:
    a = c
    if a == "O" or a == "D":
        a = "0"
    elif a == "I":
        a = "1"
    elif a == "Z":
        a = "2"
    elif a == "S":
        a = "5"
    elif a == "B":
        a = "8"
    ans += a
print(ans)
