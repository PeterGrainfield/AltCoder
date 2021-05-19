s = input()

times = {}

for c in s:
    if c not in times.keys():
        times[c] = 0
    times[c] += 1

ans = True
for t in times.values():
    if t % 2 != 0:
        ans = False
        break
print("Yes" if ans else "No")
