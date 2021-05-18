X = int(input())

y = 0
saving = 100
while saving < X:
    saving = saving * 101 // 100
    y += 1

print(y)
