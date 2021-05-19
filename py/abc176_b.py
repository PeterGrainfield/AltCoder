N = input()

s = 0
for i in range(len(N)):
    s += int(N[i])

print("Yes" if s % 9 == 0 else "No")
