s = list(input())

delim = ""
for c in s:
    if c == "C":
        delim += c
    elif c == "F" and len(delim) > 0:
        if delim[-1] == "C":
            print("Yes")
            break
else:
    print("No")