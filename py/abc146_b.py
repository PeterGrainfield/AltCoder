N = int(input())
S = input()

ans = ""
for c in S:
    o = ord(c)+N
    if o > ord('Z'):
        o -= 26
    ans += chr(o)

print(ans)
