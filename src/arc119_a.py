N = int(input())

bmax = 0
for i in range(100):
    if 2**i > N:
        bmax = i
        break
b = 0
ans = N
for j in range(bmax):
    a = N // (2**j)
    c = N - a*(2**j)
    ans = min(ans, j + a + c)

print(ans)
