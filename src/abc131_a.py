S = list(map(int, input()))

for i in range(1, 4):
    if S[i] == S[i-1]:
        print("Bad")
        break
else:
    print("Good")
