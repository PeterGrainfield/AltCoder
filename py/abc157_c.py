N, M = map(int, input().split())
lsc = [list(map(int, input().split())) for _ in range(M)]

d = [""]*N
for s, c in lsc:
    if s == 1 and c == 0 and N > 1:
        d = ["-1"]
        break
    if d[s-1] != str(c) and d[s-1] != "":
        d = ["-1"]
        break
    d[s-1] = str(c)

if d[0] != "-1":
    for i in range(N):
        if d[i] == '':
            if i == 0 and N > 1:
                d[i] = "1"
            else:
                d[i] = "0"

print("".join(d))
