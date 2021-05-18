S = input()
ls = []
for c in S:
    ls.append(True if c == '1' else False)

timesW = 0
timesB = 0
alt = True
for c in ls:
    if alt == c:
        timesW += 1
    else:
        timesB += 1
    alt = not alt
print(min(timesW, timesB))
