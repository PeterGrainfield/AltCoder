N = int(input())
lab = [list(map(int, input().split())) for _ in range(N)]

lab.sort(key=lambda x: x[1])

# print(lab)

s = 0
ans = "Yes"
for a, b in lab:
    s += a
    if s > b:
        ans = "No"
        break
print(ans)
