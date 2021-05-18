N, X = map(int, input().split())
S = input()
point = X
for c in S:
    if c == "o":
        point += 1
    elif point != 0:
        point -= 1
print(point)
