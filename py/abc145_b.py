N = int(input())
S = input()

if len(S) % 2 != 0:
    print("No")
    exit()

if S[0:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")
