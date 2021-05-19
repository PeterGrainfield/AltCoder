N = int(input())
words = []
for i in range(N):
    words.append(input())

said = [words[0]]
ans = True

for i in range(1, N):
    if words[i][0] != words[i-1][-1] or words[i] in said:
        ans = False
        break
    said.append(words[i])
    # print(said)

print("Yes" if ans else "No")
