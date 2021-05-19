# 0 <= A, B, C, D <=9
li = list(map(int, input().split()))

li.sort(reverse=True)
m = li[0]
b = li[1]
c = li[2]
dif = abs(m-b) + abs(m-c)

print(dif//2 + 2*(dif % 2))
