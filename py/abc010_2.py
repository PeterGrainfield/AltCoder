n = int(input())
la = list(map(int, input().split()))

dic = {0: 0, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}
ans = 0
for a in la:
    sp = (a - 1) % 6

    if sp != 0 and sp != 2:
        ans += dic[sp]

print(ans)
