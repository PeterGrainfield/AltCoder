# 2 <= N <= 10**5, 1 <= ai <= N
N = int(input())
la = list(map(int, input().split()))

love = 0
for i in range(N):
    if la[la[i]-1] == i + 1:
        love += 1
print(love // 2)
