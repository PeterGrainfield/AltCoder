S = input()
correct = "CODEFESTIVAL2016"

ans = 0
for i in range(16):
    if S[i] != correct[i]:
        ans += 1
print(ans)