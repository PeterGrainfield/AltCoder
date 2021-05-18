ls = list(map(str, input().split()))

lr = []
for s in ls:
    if s == "Left":
        lr.append("<")
    elif s == "Right":
        lr.append(">")
    elif s == "AtCoder":
        lr.append("A")

print(" ".join(lr))
