N = int(input())

d1 = set()
d2 = set()

for i in range(N):
    s = input()

    if s[0] == '!':
        d2.add(s[1:])
    else:
        d1.add(s)

d = list(d1 & d2)
if len(d) > 0:
    print(d[0])
else:
    print("satisfiable")
