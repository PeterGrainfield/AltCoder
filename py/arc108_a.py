S, P = map(int, input().split())

ans = False
if S > 1:
    for i in range(1, int(P**0.5)+1):
        if i * (S-i) == P:
            ans = True
            break
print("Yes" if ans else "No")
