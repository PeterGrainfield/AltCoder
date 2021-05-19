n = int(input())
h_list = list(map(int, input().split()))

low = 0
ans = True
for h in h_list:
    if low < h - 1:
        low = h - 1
    elif low > h:
        ans = False
        break
print("Yes" if ans else "No")
