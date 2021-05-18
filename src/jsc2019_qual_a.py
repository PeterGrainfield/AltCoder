M, D = map(int, input().split())

ans = 0
for month in range(1, M+1):
    for day in range(1, D+1):
        d1 = day % 10
        d10 = day//10
        if d1 >= 2 and d10 >= 2 and month == d1*d10:
            # print(month, day)
            ans += 1

print(ans)
