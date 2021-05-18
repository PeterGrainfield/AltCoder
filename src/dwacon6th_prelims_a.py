N = int(input())
lst = []
for i in range(N):
    s, t = input().split()
    lst.append([s, int(t)])

X = input()

ans = 0
for st in lst:
    if st[0] == X:
        ans = 0
    else:
        ans += st[1]

print(ans)