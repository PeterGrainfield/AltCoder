N, A, B, C, D = map(int, input().split())
s = list(input())

for i in range(B, D):
    # print(s[i], s[i+1])
    if s[i] == "#" and s[i+1] == "#":
        print("No")
        exit()
ex = False
if C > D:
    for i in range(B-2, D-1):
        # print(s[i:i+3])
        if s[i:i+3] == [".", ".", "."]:
            ex = True
else:
    ex = True

for j in range(A-1, C):
    # print(s[j], s[j+1])
    if s[j] == "#" and s[j+1] == "#":
        print("No")
        exit()
if ex:
    print("Yes")
else:
    print("No")
