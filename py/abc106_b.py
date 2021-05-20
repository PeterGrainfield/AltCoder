N = int(input())

f = 105
ans = 0
for i in range(f, N+1):
    if i % 2:
        div = 2
        for j in range(2, i):
            if i % j == 0:
                div += 1
        if div == 8:
            ###
            # print(i)
            ###
            ans += 1
print(ans)
