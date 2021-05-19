la = []
for i in range(5):
    la.append(int(input()))

k = int(input())

for a in range(5):
    for b in range(5):
        if k < abs(la[a]-la[b]):
            print(":(")
            exit()

print("Yay!")
