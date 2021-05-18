t, N = map(int, input().split())

cnt = 0
s, sp = divmod(100*N, t)
# print(s, sp)
if sp == 0:
    print(s * (100 + t) // 100 - 1)
else:
    print((s+1) * (100 + t) // 100 - 1)
