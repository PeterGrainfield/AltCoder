ls = list(map(str, input().split()))

ans = ""
for word in ls:
    ans += word[0].upper()
print(ans)